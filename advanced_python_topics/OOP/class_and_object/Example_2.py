# Exercise 2: Create a Student Class
# Create a Student class with:name, roll_number, and marks attributes. A method is_passed() that returns True if marks >= 40


class Student:

    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def is_passed(self):
        if self.marks >= 40:
            return True
        else:
            return False
    

    def display_student(self):
        print(f"Name : {self.name} Roll No : {self.roll_no} Marks : {self.marks}")

        if self.is_passed():
            print(f"Congratulations you have passed the exam {self.name}")
        else:
            print(f"You have failed the exam {self.name}")

s = Student("Ali", 101, 30)
s.display_student()
s = Student("Sarah", 102, 50)
s.display_student()

