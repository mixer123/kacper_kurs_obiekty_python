def cos(*args, name='Adam'):
    print(args)
    print(name)
# Uwaga
cos(1,2,3)
# ale jak zrobię
cos(1,2,3, 'Piotr')
# to Piotr wpadnie do tupli args
cos(1,2,3, name='Piotr') # to nadpisuje argument name 