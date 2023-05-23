import base64
import json
from ServerClient import *


def zip_xor(b1: bytes, b2: bytes) -> bytes:
    return bytes(a ^ b for a, b in zip(b1, b2))


def xor(chunks: list[bytes]) -> bytes:
    start = chunks[0]
    for chunk in chunks[1:]:
        start = zip_xor(start, chunk)
    return start


class OraclePaddingDecryptor(object):
    __AES_BLOCK_SIZE = 16

    def __init__(self, ciphertext: str, website: str):
        self.cipher_bytes = base64.b64decode(ciphertext)
        self.website = website

    def decrypt_bytes(self) -> bytes:
        result = b''
        ciphertext_chunks = self.split_ciphertext_into_blocks()
        # Going from the last element of list to the 2nd
        for i in range(len(ciphertext_chunks) - 1, 0, -1):
            result = self.decrypt_single_chunk(ciphertext_chunks[i-1], ciphertext_chunks[i]) + result
            print(result)
        return result

    def split_ciphertext_into_blocks(self) -> list:
        chunk_list = []
        length = len(self.cipher_bytes)
        for i in range(0, length - 1, self.__AES_BLOCK_SIZE):
            chunk_list.append(self.cipher_bytes[i:(i + self.__AES_BLOCK_SIZE)])
        return chunk_list

    def decrypt_single_chunk(self, chunk_i_minus_1: bytes, chunk_i: bytes) -> bytes:
        result = b''
        for i in range(0, self.__AES_BLOCK_SIZE):
            # it's impossible to directly increment a bytes object, so we'll use an integer, increment it and then
            # convert it to a byte
            curr_byte = 255
            chunks = [chunk_i_minus_1, self.prepare_pkcs7_xor_block(i + 1),
                      self.prepare_sneaky_bytes(curr_byte, result)]
            c_prim = xor(chunks) + chunk_i
            encoded = base64.b64encode(c_prim)
            while self.send_request(encoded) != 'True':
                curr_byte -= 1
                chunks[2] = self.prepare_sneaky_bytes(curr_byte, result)
                c_prim = xor(chunks) + chunk_i
                encoded = base64.b64encode(c_prim)
            # We want to append at the beginning, not the end, hence no "+="
            result = int.to_bytes(curr_byte, byteorder='big', length=1) + result
            print(result)
        return result

    def prepare_pkcs7_xor_block(self, value: int) -> bytes:
        if value < 1 or value > 16:
            raise ValueError("AES PKCS7 padding consists of bytes with value from 1 to 16")
        return (self.__AES_BLOCK_SIZE - value) * b'\x00' + value * int.to_bytes(value, byteorder='big', length=1)

    def prepare_sneaky_bytes(self, curr_byte: int, curr_result: bytes) -> bytes:
        return (self.__AES_BLOCK_SIZE - len(curr_result) - 1) * b'\x00' +\
            int.to_bytes(curr_byte, byteorder='big', length=1) + curr_result

    def send_request(self, data: bytes) -> str:
        client = ServerClient(self.website)
        headers = {'Content-type': 'application/json'}
        json_dict = {'ciphertext': data.decode('utf-8')}
        json_data = json.dumps(json_dict)
        return client.send_post('/checkpadding', json_data, headers)
