names = ['Ala', 'Mirek']
char = input('Podaj literę')
names_a = filter(lambda names: names[0].lower()==char, names)
print(list(names_a))