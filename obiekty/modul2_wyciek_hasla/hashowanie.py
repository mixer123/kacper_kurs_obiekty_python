from hashlib import sha1
text1 = 'FkdaT4LugPf5D3@'
text2= 'I&wg$S%xsT83#8'
hash1 = sha1(text1.encode('utf-8'))
hash2 = sha1(text2.encode('utf-8'))
# print(help(hash1)) # wyświetla opis dla hash1

print(len(hash2.hexdigest()))
print(hash2.hexdigest())

