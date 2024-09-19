class Rectangle:

    def __init__(self, width, length):
        self.width = width 
        self.length = length

    def area(self):
        return self.width * self.length

r1 = Rectangle(2, 4)
print(r1.area())

r2 = Rectangle(3, 5)
print(r2.area())