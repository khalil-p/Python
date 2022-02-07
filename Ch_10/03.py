class Sample:
    a = "ClassAttribute"

    def b(self):
        print(self.a)


obj = Sample()
obj.a = 0
print(Sample.a)
print(obj.a)
