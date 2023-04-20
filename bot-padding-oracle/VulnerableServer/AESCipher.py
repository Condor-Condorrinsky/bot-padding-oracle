import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

class AESCipher(object):

    def __init__(self, key, iv):
        self.bs = AES.block_size
        self.key = key
        self.iv = iv

    def encrypt(self, raw):
        raw = pad(bytes(raw, 'utf-8'), 16, style='pkcs7')
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        return base64.b64encode(cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        return unpad(cipher.decrypt(enc), 16, style='pkcs7').decode('utf-8')
