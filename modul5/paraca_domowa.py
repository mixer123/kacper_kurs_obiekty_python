''' Stwórzmy aplikację konsolową, która będzie potrafiła
szyfrować pojedyncze pliki lub wszystkie pliki w określonych
przez nas folderach.'''
from cryptography.fernet import Fernet
import  base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from os import walk, makedirs, rmdir
from os import listdir
from os.path import isfile, join

class Common:
    SALT = b'Python'  # salt w bajtach
    PASSWORD = b'Mirek123!'
    def __init__(self, name_file):
        self.name_file = name_file

    def read(self):
        with open(self.name_file, 'r') as file:
            text = file.read()
        return text
    def read_bytes(self):
        with open(self.name_file, 'r') as file:
            text = file.read()
            text=bytes(text)
        return text

    def create_key(self):

        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=Common.SALT,
            iterations=390000
        )
        key = base64.urlsafe_b64encode(kdf.derive(Common.PASSWORD))
        return key

class FileDecrypt(Common):


    pass


class FileEncrypt(Common):



    def encrypt_file(self):

        onlyfiles = [f for f in listdir('../modul5') if isfile(join('../modul5', f)) and f[-3:]=='txt']
        # print(onlyfiles)

        fernet = Fernet(self.create_key(Common.PASSWORD))
        text = self.read()
        encrypt_text = fernet.encrypt(text.encode('utf8'))
        with open(self.name_file,'w') as file:
            text= file.write(encrypt_text.decode('utf8'))
        return encrypt_text # funkcja zwraca zakodowany i zszyfrowany text w bytach

    # def decrypt_file(self):
    #     salt = b'Python'  # salt w bajtach
    #     password = b'Mirek123!'
    #     kdf = PBKDF2HMAC(
    #         algorithm=hashes.SHA256(),
    #         length=32,
    #         salt=salt,
    #         iterations=390000
    #     )
    #     fernet = Fernet(base64.urlsafe_b64encode(kdf.derive(password)))
    #     with open(self.name_file,'r') as file:
    #         text= file.read()
    #     print('text',  type(text))
    #     print('encrypt_file', fernet.decrypt(self.encrypt_file()))
    #     print(fernet.decrypt(self.encrypt_file()).decode('utf8'))
    #
    #     # print(type(text))
    #
    #     # newtext = fernet.decrypt(text).decode('utf8')
    #     # print(newtext)
    #     # with open(self.name_file,'w') as file:
    #     #     file.write(newtext)
    #
    #     # fernet.decrypt(zaszyfrowane).decode('utf8'))

file=FileEncrypt('plik_do_pracy_domowej.txt')
filedecrypt = FileDecrypt('plik_do_pracy_domowej.txt')
# print(file.read())
print(file.encrypt_file())
print(filedecrypt.read_bytes())
