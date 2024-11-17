

class Animal:
    def __init__(self, name):
        self.name = name

    def showName(self):
        print(f"{self.name}")


# here is the method with different parameter -------------

class Dog(Animal):
    def __init__(self, name, color=None):
        super().__init__(name)
        self.color = color

    def showName(self):
        if self.color is None:
            print("color None")
        print(f"{self.name} and Color : {self.color}")


animal = Animal("XAP")
animal.showName()


dog = Dog("AXis", "red")
dog.showName()
