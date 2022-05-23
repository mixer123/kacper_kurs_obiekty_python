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

    PASSWORD = b'Mirek123!'
    def __init__(self, name_file, name_file_salt):
        self.name_file = name_file
        self.name_file_salt = name_file_salt
    def read_salt(self):
        with open(self.name_file_salt, 'r') as salt:
            salt1 = bytes(salt.read().encode('utf8'))
        return salt1

    def read(self):
        with open(self.name_file, 'r') as file:
            text = file.read()
        return text
    def read_bytes(self):
        with open(self.name_file, 'r') as file:
            text = file.read().encode('utf8')
            text=bytes(text)
        return text

    def create_key(self, password):

        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.read_salt(),
            iterations=390000
        )
        key = base64.urlsafe_b64encode(kdf.derive(password))
        return key

class FileDecrypt(Common):
    def decrypt_file(self):
        with open(self.name_file, 'r') as file:
            text = file.read()
        fernet = Fernet(self.create_key(Common.PASSWORD))
        fernet_content = fernet.decrypt(text.encode('utf8'))
        with open(self.name_file,'w') as file:
            file.write(fernet_content.decode('utf8'))


class FileEncrypt(Common):
    def encrypt_file(self):
        # onlyfiles = [f for f in listdir('../modul5') if isfile(join('../modul5', f)) and f[-3:]=='txt']
        # print(onlyfiles)
        fernet = Fernet(self.create_key(Common.PASSWORD))
        text = self.read()
        encrypt_text = fernet.encrypt(text.encode('utf8'))
        with open(self.name_file,'w') as file:
            text= file.write(encrypt_text.decode('utf8'))
        return encrypt_text # funkcja zwraca zakodowany i zszyfrowany text w bytach



file=FileEncrypt('plik_do_pracy_domowej.txt', 'salt.txt')
file.read_salt()
filedecrypt = FileDecrypt('plik_do_pracy_domowej.txt', 'salt.txt')

file.encrypt_file()

# filedecrypt.decrypt_file()
