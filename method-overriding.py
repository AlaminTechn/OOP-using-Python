

class Animal:
    def __init__(self, name):
        self.name = name

    def showName(self):
        print(f"{self.name}")


class Dog(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def showName(self):
        print(f"{self.name} and Color : {self.color}")


animal = Animal("XAP")
animal.showName()


dog = Dog("AXis", "red")

dog.showName()


# here is the same method and same parameter in parent and child class
