import sys
def suma(a=2,b=2,*args):
    wynik = a+b
    for arg in args:
        wynik +=arg
    return wynik
# print(suma(3,4,4,6,8))
'''Zapisujemy do pliku jak standardowe wyjście, print pisze po pliku nie po ekranie'''
original_stdout = sys.stdout
file1 = open('file.txt', 'w')
sys.stdout = file1
print(file=file1)
print('Hello, Python!')
file1.close()
sys.stdout = original_stdout