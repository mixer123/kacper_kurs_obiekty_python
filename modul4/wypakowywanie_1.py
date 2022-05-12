a, *b, c =(1,2,3,4)
''' a przypisze pierwszy element, c przypisze ostatni element b wezmie co mu zostanie'''
print(a)
print(b)
print(c)

a, *c, d,  ='alass'
print(a)

print(c)
print(d)

def my_func(a,b,c):
    print('-'*10)
    print(a)
    print(b)
    print(c)
my_data = (1,2,3)
my_func(*my_data)