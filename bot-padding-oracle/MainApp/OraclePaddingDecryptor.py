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
    
    def decrypt_single_chunk(self, byteschunk: bytes):
        # it's impossible to directly increment a bytes object, so we'll use an integer, increment it and then convert it to a byte
        curr_byte = 0
        # sneaky_bytes = random.randbytes(15)
        sneaky_bytes = b'000000000000000'
        concatenation = base64.b64encode(sneaky_bytes + self.int_to_byte(curr_byte) + byteschunk)
        while ((result := self.send_request(concatenation)) != 'True'):
            print(str(curr_byte) + ': ' + result)
            curr_byte += 1
            concatenation = base64.b64encode(sneaky_bytes + self.int_to_byte(curr_byte) + byteschunk)
        return curr_byte
        
    def int_to_byte(self, num: int):
        return num.to_bytes(1, byteorder='big')

    def send_request(self, data: bytes) -> str:
        client = ServerClient(self.website)
        headers = {'Content-type' : 'application/json'}
        json_dict = {'ciphertext' : data.decode('utf-8')}
        json_data = json.dumps(json_dict)
        return client.sendPOST('/checkpadding', json_data, headers)
