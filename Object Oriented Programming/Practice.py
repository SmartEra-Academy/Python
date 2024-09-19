class Student:
    def __init__(self, name, age, student_id):
        self.name = name  
        self.age = age  
        self.student_id = student_id  
        self.courses_enrolled = []  # List to hold the courses the student is enrolled in

    # Method to enroll the student in a course
    def enroll_course(self, course):
        self.courses_enrolled.append(course)

    # Method for the student to introduce themselves
    def introduce(self):
        print(f"Hi, I am {self.name}, I am {self.age} years old, and my student ID is {self.student_id}.")

    # Method to list the courses the student is enrolled in
    def enrolled_courses(self):
        if self.courses_enrolled:
            print(f"Enrolled Courses of {self.name} are: {', '.join(self.courses_enrolled)}")
        else:
            print(f"{self.name} is not enrolled in any courses yet.")


# Create the first student and enroll them in courses
s1 = Student("Ali", 23, 3257)

s1.introduce()

s1.enroll_course("Math")
s1.enroll_course("Science")
s1.enroll_course("History")

s1.enrolled_courses()

print()

# Create the second student and enroll them in courses
s2 = Student("Reza", 24, 3347)

s2.introduce()

s2.enroll_course("Geography")
s2.enroll_course("Math")

s2.enrolled_courses()
