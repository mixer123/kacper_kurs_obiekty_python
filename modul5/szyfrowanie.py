from cryptography.fernet import Fernet
import  base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
password = b'Mirek123!'
salt = b'Python' # salt w bajtach
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=390000
)
# print(base64.urlsafe_b64encode(kdf.derive((password)))) # hashowanie hasła
# Szyfrowanie

# base64.urlsafe_b64encode(kdf.derive(password))  TO JEST KLUCZ
fernet = Fernet(base64.urlsafe_b64encode(kdf.derive(password)))
# To bedziemy szyfrowac
text = input('Podaj cos do zaszyfrowania:')
zaszyfrowane=fernet.encrypt(text.encode('utf8'))
print(zaszyfrowane.decode('utf8'))
# Odszyfrowanie
print(fernet.decrypt(zaszyfrowane).decode('utf8'))