def suma(numbers):
    suma = 0
    for num in numbers:
        suma += num
    return suma


def do_something(numbers, fun):
    return fun(numbers)


print(do_something([1,2,3],suma))