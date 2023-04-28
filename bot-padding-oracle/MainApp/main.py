from OraclePaddingDecryptor import *

if __name__ == '__main__':
    example_cipher = \
        '3k74e8Ie12G8I3tmPrHowXMdnSFyI3Ipkbwjgr03GATqQU+kuU4Mu1gtAY/SJ+tbR9B6j7lYU7CIhgoDcYDsqVuKrLK+ZMK2rHJZpcASKiE='
    serv = '127.0.0.1:5000'
    decryptor = OraclePaddingDecryptor(example_cipher, serv)
    blocks = decryptor.split_ciphertext_into_blocks()
    print(decryptor.decrypt_single_chunk(blocks[-2], blocks[-1]))
