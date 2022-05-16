class Osoba:
    def __init__(self, name):
        self.name = name
        self.age = 34
def func_attr(field_name):
    adam = Osoba('mirek')
    return getattr(adam, field_name)

print(func_attr('name')) # w '' jest nazwa pola 
print(func_attr('age'))
# adam = Osoba("mirek")
# print(adam.name)
# x = getattr(adam, 'name')
# print(x)