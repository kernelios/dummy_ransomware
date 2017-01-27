import base64
from Crypto.Cipher import AES
from Crypto import Random


class AESCipher:
    """includes AES encryption and decryption methods.
    one property:
     key - the encryption decryption key."""


    # encryption padding
    block_size = 16
    pad_value = lambda self, x: x + (self.block_size - len(x) % self.block_size) * \
                              chr(self.block_size - len(x) % self.block_size)
    unpad_value = lambda self, x: x[:-ord(x[len(x) - 1:])]

    def __init__( self, key):
        """constructor to set the key property"""
        self.__key = key

    def get_key(self):
        """Getter for key property"""
        return  self.__key

    def encrypt(self, data):
        """encrypt given data"""
        data = self.pad_value(data)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(data))

    def decrypt(self, data):
        """decrypt given data"""
        data = base64.b64decode(data)
        iv = data[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self.unpad_value(cipher.decrypt(data[16:]))