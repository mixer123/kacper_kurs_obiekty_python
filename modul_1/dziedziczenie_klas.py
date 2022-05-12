class Person:
    def __init__(self, name, familyname):
        self.name = name
        self.familyname = familyname

    def hello(self):
        return f'witaj {self.name} {self.familyname} '


class Student(Person):
    def __init__(self, name, familyname):
        super().__init__(name, familyname)


student = Student('mirek', 'girek')
print(student.hello())


#
#
# person = Person("mirek", 'girek')
# print(person.hello())
