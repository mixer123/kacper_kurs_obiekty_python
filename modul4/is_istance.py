from typing import Union

class Person:
    pass
class Osoba(Person):
    pass
person = Person()
osoba = Osoba()
def my_fun(x):
    if isinstance(osoba,Person):
        print('ok')
    else:
        print('not ok')
my_fun(osoba)
