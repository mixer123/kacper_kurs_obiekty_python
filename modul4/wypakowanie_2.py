data = {'a':1,'b':2,'c':3}
a,b,c = data.keys()
print(a)
print(b)
print(c)

def my_func(a,b,c):
    print(a)
    print(b)
    print(c)
data_dict = {'a':1,'c':2,'b':3}
# my_func(*data_dict) # wypakowanie kluczy slownika
my_func(**data_dict) # wypakowanie wartosci slownika
