def cos(*args, name='name',**kwargs):
    print(args)
    print(name)
    print(kwargs)

cos(1,2,3)
cos(2,3,4,name='Mirek', kwargs='cos', kw='fdfd')
''' Args są w postaci tupli,  kwargs jest w postaci slownika
Argumenty nazwane muszą być przed kwargs'''