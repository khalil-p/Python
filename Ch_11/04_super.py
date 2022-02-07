class Person:
    country = "India"
    company = "Google"

    def __init__(self):
        print("Initializing Person...")

    def takeBreath(self):
        print("I am breathing...")


class Employee(Person):
    company = "Honda"

    def getSalary(self):
        super().__init__()
        print(f"The salary is {self.salary}")

    def takeBreath(self):
        super().takeBreath()
        print("I am an employee so I am luckily breathing...")


class Programmer(Employee):
    company = "Fever"

    @staticmethod
    def getSalary(self):
        print(f"No salary to programmers")

    def takeBreath(self):
        super().takeBreath()
        print("I am brithing ++..")


p = Person()
# p.takeBreath()
e = Employee()
print(e.company)
# e.takeBreath()
# pr = Programmer()
# pr.takeBreath()
