fruits =['jablko','banan']
length = [len(i) for i in fruits]

mapowanie = map(len, fruits)
print(list(mapowanie))