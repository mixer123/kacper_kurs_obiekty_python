from collections import namedtuple

User = namedtuple('user', 'name')
person = User('mirek')

print(person.name)