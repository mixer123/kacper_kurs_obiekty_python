import requests


url = 'https://api.pwnedpasswords.com/range/9b76f'
r = requests.get(url, allow_redirects=True)

open('../modul2_wyciek_hasla/hash.txt', 'wb').write(r.content)