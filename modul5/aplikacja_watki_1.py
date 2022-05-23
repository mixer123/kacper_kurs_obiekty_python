class DoSomething:
    def __init__(self, name):
        self.name = name

    def run(self):
        for i in range(8):
            print(f'{self.name}->{i}')
job1 = DoSomething('job1')
job1.run()

job2 = DoSomething('job2')
job2.run()

job3 = DoSomething('job3')
job3.run()