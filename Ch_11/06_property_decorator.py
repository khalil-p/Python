class Employee:
    company = "Google"
    salary = 5000
    salaryBonus = 800
    # totalSalary = 5800

    @property
    def totalSalary(self):
        return self.salary + self.salaryBonus

    @totalSalary.setter
    def totalSalary(self, value):
        self.salaryBonus = value - self.salary


e = Employee()
print(e.totalSalary)
e.totalSalary = 6100
print(e.salary)
print(e.salaryBonus)
