import re
import requests
from hashlib import sha1
import logging


class Password:
    # def __init__(self):
    #     pass


    def big_char(self, password):
        count = 0
        for char in password:
            if char.isupper():
                count += 1
        if count > 0:
            return True
        return False

    def check_special_sign(self, password):
        special_sign = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        if (special_sign.search(password) == None):
            return False
        return True

    def length(self, password):
        if len(password) > 7:
            return True
    def at_least_one_number(self, password):
        count_number = 0
        for i in password:
            if i in '1234567890':
                count_number +=1
        if count_number > 0:
            return True
        return False

    def good_password(self, file1, file2):
        with open(file2, 'a') as file_2:
            file_2.truncate(0)
        with open(file1,'r') as file_1:
            passwords = file_1.readlines()
        for password in passwords:
            if self.length(password) and self.at_least_one_number(password) \
                    and self.check_special_sign(password) and self.big_char(password) and self.is_password_out(password)==False:
                with open(file2,'a') as file_2:
                    file_2.write(password)

            else:
                with open(file2,'a') as file_2:
                    file_2.write(password)




    # Sprawdzam czy hasło wyciekło za pomocą api

    def is_password_out(self, password):
        with open('hash.txt', 'a') as file_2:
            file_2.truncate(0)
        hash = sha1(password.encode('utf-8'))
        logger = logging.getLogger()
        handler = logging.FileHandler(str(hash.hexdigest())[0:5] + '.txt')
        logger.addHandler(handler)
        with open(str(hash.hexdigest())[0:5] + '.txt', 'a') as file_3:
            file_3.truncate(0)
        url = 'https://api.pwnedpasswords.com/range/'+str(hash.hexdigest())[0:5]
        r = requests.get(url, allow_redirects=True)
        open('hash.txt', 'wb').write(r.content)
        with open('hash.txt', 'r') as file_1:
            passwords = file_1.readlines()
            for line in passwords:
                password_hash = str(hash.hexdigest())[0:5]+line.split(':')[0]
                if hash.hexdigest() == password_hash:
                    logger.error(f'Hasło wyciekło {str(hash.hexdigest())}')
                    return True
        logger.error(f'Hasło  {str(hash.hexdigest())} bezpieczne')
        logging.getLogger().removeHandler(logging.getLogger().handlers[0])
        return False

password = Password()
password.good_password('passwords.txt','bezpieczne.txt')