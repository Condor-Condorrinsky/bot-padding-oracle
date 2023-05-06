import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


class AESCipher(object):
    __AES_BLOCK_SIZE = 16

    def __init__(self, key, iv):
        self.bs = AES.block_size
        self.key = key
        self.iv = iv

    def encrypt(self, raw):
        raw = pad(bytes(raw, 'utf-8'), self.__AES_BLOCK_SIZE, style='pkcs7')
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        return base64.b64encode(cipher.encrypt(raw))

    def decrypt(self, enc):
        decoded = base64.b64decode(enc)
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        decrypted = cipher.decrypt(decoded)
        unpadded = unpad(decrypted, self.__AES_BLOCK_SIZE, style='pkcs7')
        # Ugly as hell, but both in the case of wrong padding and correct padding, but the inability to decode the
        # message pycryptodome throws the same ValueError exception and I need to differentiate those cases
        try:
            decoded = unpadded.decode('utf-8')
        except ValueError:
            raise TypeError('Malformed message')
        return decoded
