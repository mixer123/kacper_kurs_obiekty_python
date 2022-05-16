value1 = 1
valeu2 =2

slownik ={
    'dodaj': lambda a,b: a+b,
    'odejmij': lambda a,b: a-b,
    'pomnoz': lambda a,b: a*b
}

function = slownik['dodaj']
print(function(valeu2, value1))

# Można też na obiekcie

class Calculator:
    def __init__(self, a , b):
        self.a = a
        self.b = b
    def do_it(self):
        return self.a + self.b
calc = Calculator(3,4)

slownik1 ={
    'dodaj': calc.do_it,
    'odejmij': lambda a,b: a-b,
    'pomnoz': lambda a,b: a*b
}

function1 = slownik1['dodaj']
print('do it', function1()) # musi być nawias ()