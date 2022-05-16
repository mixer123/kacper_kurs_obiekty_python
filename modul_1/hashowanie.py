from hashlib import sha1
text1 = 'adam'
text2= 'mirek'
hash1 = sha1(text1.encode('utf-8'))
hash2 = sha1(text2.encode('utf-8'))
# print(help(hash1)) # wyświetla opis dla hash1
print(hash1.hexdigest())
print(hash2.hexdigest())