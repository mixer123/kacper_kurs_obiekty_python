import re
def big_char(password):
    count = 0
    for char in password:
        if char.isupper():
            count += 1
    if count > 0:
        return True
    return False

def check_special_sign(password):
    special_sign = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if (special_sign.search(password) == None):
        return False
    return True

def length(password):
    if len(password) > 7:
        return True
def at_least_one_number(password):
    count_number = 0
    for i in password:
        if i in '1234567890':
            count_number +=1
    if count_number > 0:
        print(count_number)
        return True
    return False

def good_password(file1, file2):
    with open(file2, 'a') as file_2:
        file_2.truncate(0)
    with open(file1,'r') as file_1:
        passwords = file_1.readlines()
    for password in passwords:

        if length(password) and at_least_one_number(password) \
                and check_special_sign(password) and big_char(password):

            with open(file2,'a') as file_2:

                file_2.write(password)
good_password('passwords.txt','bezpieczne.txt')

