from requests import  get

currency = input('Podaj kurs walut')
# url = 'http://api.nbp.pl/api/exchangerates/rates/a/'+currency+'/last/'

url = 'http://api.nbp.pl/api/exchangerates/rates/a/'+currency+'/last/10/?format=json'

with get(url) as content:
    # print(content)
    for cont in content:

        print(((cont.decode().split(''))))


