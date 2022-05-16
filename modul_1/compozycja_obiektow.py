class Car:
    def __init__(self, brand, capacity):
        self.brand = brand
        self.engine =  Engine(capacity)

class Engine:
    def __init__(self, capacity):
        self.capacity = capacity


engine = Engine(3.2)
car = Car('opel',4.2)
print(car.engine.capacity)