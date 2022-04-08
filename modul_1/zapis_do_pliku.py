import logging
class Write_to_file:
    def __init__(self, name, name2):
        self.name = name
        self.name2 = name2
    # def read(self):
    #     with open(self.name, mode='w') as file:



    def write(self):
        with open(self.name2) as file2:
            text= file2.read()
        with open(self.name, mode='w') as file:

            file.write(text)

write = Write_to_file('file.txt','open.txt')
(write.write())


