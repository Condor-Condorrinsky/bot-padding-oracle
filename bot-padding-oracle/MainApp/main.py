from OraclePaddingDecryptor import *

if __name__ == '__main__':
    example_cipher = 'Rqbab1+Xsm1UXl/KdK2/ZllX4VH3WvLlzoTmGgDQGHg='
    serv = '127.0.0.1:5000'
    decryptor = OraclePaddingDecryptor(example_cipher, serv)
    blocks = decryptor.split_ciphertext_into_blocks()
    print(decryptor.decrypt_single_chunk(blocks[0]))
