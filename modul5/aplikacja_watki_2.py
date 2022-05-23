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