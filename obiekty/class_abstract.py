'''  Klasy abstrakcyjne są po to aby wymuszać na innych klasach pewien
standard ustalony w klasie abstrakcyjnej'''

from abc import ABC, abstractmethod
class ValidatorInterface(ABC):
    ''' Metoda validate jest metodą abstrakcyjną. W klasie potomnej
    będzie musiała być metoda validate'''
    @abstractmethod
    def validate(self):
        pass
class Validate(ValidatorInterface):
    def validate(self):
        return 'To jest przykład klasy potomnej'

validate =Validate()
print(validate)