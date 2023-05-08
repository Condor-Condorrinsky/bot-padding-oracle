from OraclePaddingDecryptor import *

if __name__ == '__main__':
    example_cipher = \
        'B1kn29C1MbTLTwvrykyLbvZq8DhY36oBFi3dHOvkVl0eEFug50TO5zo3WoRMC7HG3LLtrhL/6Y1LcG0EdK1hzymc8eMuaEwdJBDTdBGSgOU='
    serv = '127.0.0.1:5000'
    decryptor = OraclePaddingDecryptor(example_cipher, serv)
    blocks = decryptor.split_ciphertext_into_blocks()
    print(decryptor.decrypt_single_chunk(blocks[-2], blocks[-1]))
