import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


class AESCipher(object):

    def __init__(self, key, iv):
        self.bs = AES.block_size
        #self.key = hashlib.sha256(key).digest()
        self.key = key
        self.iv = iv

    def encrypt(self, raw):
        raw = pad(bytes(raw, 'utf-8'), 16, style='pkcs7')
        #iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        #return base64.b64encode(self.iv + cipher.encrypt(raw))
        return base64.b64encode(cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        #iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        #return unpad(cipher.decrypt(enc[AES.block_size:]), 16, style='pkcs7').decode('utf-8')
        return unpad(cipher.decrypt(enc), 16, style='pkcs7').decode('utf-8')
