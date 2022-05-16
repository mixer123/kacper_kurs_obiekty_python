'''Context manager kojarzy się z with
To jest cos z czymś sie łączymy cos robimy i rozłaczamy się
np . plik , baza, serwer poczty
'''
#
# class FirstContextManager:
#     def __init__(self):
#         print("in inirt")
#
#
#     def __enter__(self):
#         print('in enter')
#         return self
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('in exit')
# ''' To już jest context manager'''
#
# with FirstContextManager() as first_context:
#     print('do job')

class SecondContextManager:
    def __init__(self, file_name):
        self.file_name = file_name
        self.myfile = None # to jest uchwyt do pliku

    def __enter__(self):
        self.myfile = open(self.file_name)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.myfile.close()
''' test.txt trafia do self w init i trzeba go odebrać
    file to jest to co zwróci __enter__'''
with SecondContextManager('test.txt')  as file:
   for line in file.myfile:
       print(line)