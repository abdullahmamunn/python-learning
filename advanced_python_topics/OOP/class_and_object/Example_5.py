# __str__()
# __repr__()
# The __str__() method is used to define a string representation of an object for end-users.
# It is called by the built-in str() function and by the print() function to convert an object to a string.
# The __repr__() method is used to define a string representation of an object for developers. It is called by the built-in repr() function and is meant to provide a detailed string representation of the object that can be used for debugging.
# The __repr__() method should return a string that, when passed to eval(), would recreate the object.

# name: underscore methods

class Student:
    def __init__(self, name, roll, department):
        self.name = name
        self.roll = roll
        self.department = department

    def __str__(self):
        return f"{self.name}, {self.roll}, {self.department}"

    def __repr__(self):
        return f"{self.name}, {self.roll}, {self.department}"
    

# Creating student objects
s1 = Student("Abdullah", 101, "Computer Science")
s2 = Student("Ayesha", 102, "Electrical Engineering")

# User-friendly print
print(s1) 

# Developer/debug-friendly view
print(repr(s1))
# print(repr(s1))  # Student(name='Abdullah', roll=101, department='Computer Science')


