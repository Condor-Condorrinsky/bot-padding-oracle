from OraclePaddingDecryptor import *

if __name__ == '__main__':
    example_cipher = 'Noum3BJFo6W8ccXykziTEpqBf0k78RZgux8zh5phIL4='
    serv = '127.0.0.1:5000'
    decryptor = OraclePaddingDecryptor(example_cipher, serv)
    blocks = decryptor.split_ciphertext_into_blocks()
    # print(decryptor.decrypt_single_chunk(blocks[0]))
    print(decryptor.send_request(b'\x12\x34\x56\x78\x90'))
