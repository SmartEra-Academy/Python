class Rectangle:

    def area(self):
        return self.width * self.length

r1 = Rectangle()
r1.width = 2
r1.length = 4
print(r1.area())