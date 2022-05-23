''' Zrobimy trzy wątki'''
import threading
class DoSomething(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        for i in range(8):
            print(f'{self.name}->{i}')
''' Start uruchamia metodę run'''
job1 = DoSomething('job1')
job1.start()

job2 = DoSomething('job2')
job2.start()

job3 = DoSomething('job3')
job3.start()
''' Użycie join spowoduje  ze print('aaaaaaaaaaaaaaaaaaaaaaaaaaaa')  Bedzie 
 zrobine na końcu. W przeciwnym wypadku będzie wykonane w ;osowej kolejnosci - 
 patrz aplikacja_watki_2.py'''
job1.join()
job2.join()
job3.join()


print('aaaaaaaaaaaaaaaaaaaaaaaaaaaa')