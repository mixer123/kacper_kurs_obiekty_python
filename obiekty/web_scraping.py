from bs4 import BeautifulSoup
from requests import get
url ='https://www.olx.pl/motoryzacja/samochody/kujawsko-pomorskie/'
page = get(url)
bs = BeautifulSoup(page.content, 'html.parser')
''' Teraz bede tworzył selektory'''
for offer in bs.find_all('div',class_='offer-wrapper'):
    footer = offer.find('td', class_='bottom-cell')
    location = footer.find('small', class_='breadcrumb').get_text().strip()
    title = offer.find('strong').get_text().strip()
    price = offer.find('p', class_='price').get_text().strip().replace(' ','').replace('zł','')
    print(location, title, price)
