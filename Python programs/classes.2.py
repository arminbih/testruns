class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print (f"Hi my name is {self.name}")

john = Person("John Smith")
john.talk()