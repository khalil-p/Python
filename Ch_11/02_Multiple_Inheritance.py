class Employee:
    company = "Google"
    eCode = 120


class Freelancer:
    company = "Fiverr"
    level = 0

    def upgradeLevel(self):
        self.level = self.level + 1
        print(self.level)


class Programmer(Freelancer, Employee):
    name = "Khalil"
    level = 2


e = Employee()
f = Freelancer()

p = Programmer()
p.upgradeLevel()
print(p.company)
