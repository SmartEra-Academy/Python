class Rectangle:

    def area(self, num):
        return "area", num
    
r1 = Rectangle()
print(r1.area(2), Rectangle.area(r1, 2))

r2 = Rectangle()
print(r2.area(3), Rectangle.area(r2, 3))