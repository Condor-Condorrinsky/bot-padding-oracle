from AESCipher import AESCipher

# AUTHOR IS AWARE THAT HARDCODING KEYS/IVS IS A TERRIBLE PRACTICE; THIS IS FOR EDUCATIONAL PURPOSES
# Exactly 32 bytes
key = bytes('Nieprawdopodobnie mocarny klucz.', 'utf-8')
# Exactly 16 bytes
iv = bytes('MocarnyWektor...', 'utf-8')


def encrypt(plaintext: str) -> bytes:
    print('---New encryption request---')
    cipher_machine = AESCipher(key, iv)
    return cipher_machine.encrypt(plaintext)


def check_padding(ciphertext: str) -> bool | None:
    print('---New padding request---')
    try:
        cipher_machine = AESCipher(key, iv)
        cipher_machine.decrypt(ciphertext)
        return True
    except TypeError as t:
        print(t)
        return True
    except ValueError as v:
        print(v)
        return False
    except Exception as e:
        print(e)
        return None
