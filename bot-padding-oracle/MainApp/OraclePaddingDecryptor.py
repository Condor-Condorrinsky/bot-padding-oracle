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
            chunk_list.append(self.ciphertbytes[i:(i + self.__AES_BLOCK_SIZE - 1)])
        return chunk_list
    
    def decrypt_single_chunk(self, byteschunk: bytes):
        beginning_sneaky_bytes = random.randbytes(15) + b'\x99'
        concatenation = base64.b64encode(beginning_sneaky_bytes + byteschunk)
        result = self.send_request(concatenation)
        return result

    def send_request(self, data: bytes) -> str:
        client = ServerClient(self.website)
        headers = {'Content-type' : 'application/json'}
        # json_string = '{{"ciphertext":"{text}"}}'.format(text=base64.b64encode(data))
        encoded = base64.b64encode(data)
        json_dict = {"ciphertext" : str(base64.b64encode(data))}
        json_data = json.dumps(json_dict)
        return client.sendPOST('/checkpadding', json_data, headers)
