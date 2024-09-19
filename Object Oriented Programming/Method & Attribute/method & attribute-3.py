class Rectangle:

    def __init__(self, width, length):
        self.width = width 
        self.length = length

    def perimeter(self):
        return (self.width + self.length) * 2

    def area(self):
        return self.width * self.length

r1 = Rectangle(2, 4)
print(r1.area())
print(r1.perimeter())
print(r1.width, r1.length)

r2 = Rectangle(3, 5)
print(r2.area())
print(r2.perimeter())
print(r2.width, r2.length)