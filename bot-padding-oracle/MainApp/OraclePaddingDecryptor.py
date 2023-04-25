import base64
import random
import json
from ServerClient import *

class OraclePaddingDecryptor(object):

    __AES_BLOCK_SIZE = 16

    def __init__(self, ciphertext: str, website: str):
        self.ciphertbytes = base64.b64decode(ciphertext)
        self.website = website

    def decrypt_bytes(self):
        ciphertext_chunks = self.split_ciphertext_into_blocks()
        for fragment in ciphertext_chunks:
            pass
        return
    
    def split_ciphertext_into_blocks(self) -> list:
        chunk_list = []
        lngth = len(self.ciphertbytes)
        for i in range(0, lngth - 1, self.__AES_BLOCK_SIZE):
            chunk_list.append(self.ciphertbytes[i:(i + self.__AES_BLOCK_SIZE)])
        return chunk_list
    
    def zip_xor(self, b1, b2):
        return bytes(a ^ b for a, b in zip(b1, b2))
    
    def xor(self, chunks: list[bytes]):
        start = chunks[0]
        for chunk in chunks[1:]:
            start = self.zip_xor(start, chunk)
        return start
    
    def decrypt_single_chunk(self, chunk_i_minus_1: bytes, chunk_i: bytes):
        # it's impossible to directly increment a bytes object, so we'll use an integer, increment it and then convert it to a byte
        curr_byte = 0
        chunks = [chunk_i_minus_1, b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01',
                  (b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' + int.to_bytes(curr_byte))]
        c_prim = self.xor(chunks) + chunk_i
        encoded = base64.b64encode(c_prim)
        while ((result := self.send_request(encoded)) != 'True'):
            print(str(curr_byte) + ': ' + result)
            curr_byte += 1
            chunks[2] = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' + int.to_bytes(curr_byte)
            c_prim = self.xor(chunks) + chunk_i
            encoded = base64.b64encode(c_prim)
        return curr_byte

    def send_request(self, data: bytes) -> str:
        client = ServerClient(self.website)
        headers = {'Content-type' : 'application/json'}
        json_dict = {'ciphertext' : data.decode('utf-8')}
        json_data = json.dumps(json_dict)
        return client.sendPOST('/checkpadding', json_data, headers)
