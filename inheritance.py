

class Person:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def printName(self):
        print(self.firstName, self.lastName)


# create a child class from parent class

class Child(Person):
    def __init__(self, firstName, lastName, mother):
        super().__init__(firstName, lastName)
        self.mother = mother

    def printWithMotherName(self):
        print(
            f"Full Name: {self.firstName}-{self.lastName} and Mother Name: {self.mother}"
        )


class EducationInformation(Child):
    def __init__(self, firstName, lastName, mother, schoolName, roll, className):
        super().__init__(firstName, lastName, mother)

        self.schoolName = schoolName
        self.roll = roll
        self.className = className

    def showEducationInfo(self):
        print(
            f"{self.firstName}-{self.lastName},School: {self.schoolName}, Roll {self.roll}"
        )


# use Class
x = Person("Alamin", "Sarker")
x.printName()


y = Child("Afnan", "Sarker", "Atoara")
y.printWithMotherName()


z = EducationInformation("Rafi", "Alam", "Safia", "Dilalpur", 50, "XI")
z.printWithMotherName()
z.showEducationInfo()
