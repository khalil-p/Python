class Person:
    country = "India"
    company = "Google"

    def takeBreath(self):
        print("I am breathing...")


class Employee(Person):
    company = "Honda"

    def getSalary(self):
        print(f"The salary is {self.salary}")

    def takeBreath(self):
        print("I am an employee so I am luckily breathing...")


class Programmer(Employee):
    company = "Fever"

    def getSalary(self):
        print(f"No salary to programmers")


p = Person()
e = Employee()
print(e.company)
pr = Programmer()
print(pr.company)
print(pr.country)
