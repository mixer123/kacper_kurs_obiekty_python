import re
mail = 'miroslaw.butajlo@gmail.com'
expr = re.match(r'[a-z0-9.]+@[a-z.]+',mail)
def mail_validator(mail:str):
    expr = re.match(r'[a-z0-9.]+@[a-z.]+',mail)
    if expr:
        return True
    else:
        return False
print(mail_validator(mail))
'''Jeśli chcemy wyszukać w tekście mail to robimy to tak jak poniżej'''
text = 'sdsdsd miroslaw.butajlo@gmail.com'
out = re.search(r'[a-z0-9.]+@[a-z.]+', text)
if out:
    print('znalazlem')
else:
    print('nie znalazlem')