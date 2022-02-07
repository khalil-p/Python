from os import name


class Programmer:
    company = "Microsoft"

    def __init__(self, name, salary, subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit

    def getInfo(self):
        print(f"{self.name} salary is {self.salary} and subunit is {self.subunit}")


harry = Programmer("Harry", 200, "IBM")


harry.getInfo()
# class programmer:
#     company = "microsoft"

#     def employee(self):
#         print(f"The salary is {self.salary}")


# khalil = programmer()
# harry = programmer()
# khalil.salary = 1000000
# khalil.id = 'KP001'
# harry.salary = 50000
# harry.id = 'HK003'

# harry.employee()
# khalil.employee()
