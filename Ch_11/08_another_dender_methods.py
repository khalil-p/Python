class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, num2):
        return self.num + num2.num

    def __mul__(self, num2):
        return self.num * num2.num

    def __str__(self):
        return f"Decimal Number {self.num}"

    def __len__(self):
        return 1


n1 = Number(2)
n1 = Number(3)

print(n1)
print(len(n1))
