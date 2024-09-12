class Student:
    nationality = "Iran"

    def __init__(self, name, age):
        self.name = name  
        self.age = age  

s1 = Student("Sara", 20)
print(s1.name, s1.age, s1.nationality)

s2 = Student("Mohammad", 22)
print(s2.name, s2.age, s2.nationality)

s3 = Student("Reza", 23)
print(s3.name, s3.age, s3.nationality)

s3.nationality = "Italy"
print(s3.name, s3.age, s3.nationality)

print()

Student.nationality = "Canada"
print(s1.name, s1.age, s1.nationality)
print(s2.name, s2.age, s2.nationality)
print(s3.name, s3.age, s3.nationality)