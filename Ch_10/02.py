import math


class Calculator:
    calc = "calculator"

    def __init__(self, number):
        self.number = number

    def calcuate(self):
        square = self.number ** 2
        cube = self.number ** 3
        sqRoot = math.sqrt(self.number)
        print(
            f"The square of the number is {square} ,\ncube of the number is {cube} \nand the square root of the number is {sqRoot}")


calcy = Calculator(4)

calcy.calcuate()
