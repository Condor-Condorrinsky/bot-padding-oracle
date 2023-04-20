from Crypto.Random import get_random_bytes
from AESCipher import AESCipher

# Exactly 32 bytes
key = bytes('Nieprawdopodobnie mocarny klucz.', 'utf-8')
# Exactly 16 bytes
iv = bytes('MocarnyWektor...', 'utf-8')

def encrypt(plaintext: str) -> bytes:
    cipher_machine = AESCipher(key, iv)
    return cipher_machine.encrypt(plaintext)

def check_padding(ciphertext: str) -> bool:
    try:
        cipher_machine = AESCipher(key, iv)
        cipher_machine.decrypt(ciphertext)
        return True
    except ValueError:
        return False
    except Exception as e:
        print(e)
        return None
    
# if __name__ == '__main__':
#     string = encrypt("trolololo")
#     string2 = string[0:-1] + b'e'
#     string3 = "dTTriExcRXPmf8JYp/u58w=="
#     ret = check_padding(string)
#     ret2 = check_padding(string2)
#     ret3 = check_padding(string3)
#     print(ret)
#     print(ret2)
#     print(ret3)
