class Student:
    def __init__(self, name, age):
        self.name = name  
        self.age = age  

s1 = Student("Sara", 20)
print(s1.name, s1.age)

s1.name = "Zahra"
print(s1.name, s1.age)

s2 = Student("Mohammad", 22)
print(s2.name, s2.age)

s2.age = 24
print(s2.name, s2.age)