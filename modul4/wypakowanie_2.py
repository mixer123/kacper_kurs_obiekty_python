
data = {'a':1,'b':2,'c':4}
a,b,c = data.keys()
# print(a)
# print(b)
# print(c)

def my_func(a,b,c):
    print(a)
    print(b)
    print(c)
def my_func1(click): # argument musi się nazywać tak jak klucz słwonika
    print(click)

data_dict = {'a':1,'c':2,'b':[3]}
dict1 = {"click":[{"click button mouse":{"button": "left"}}]}
dict2 = {"click":2}
# my_func(*data_dict) # wypakowanie kluczy slownika
my_func(**data_dict) # wypakowanie wartosci slownika
my_func1(**dict1) # wypakowanie wartosci slownika
