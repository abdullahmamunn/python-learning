# object orieneted programming
# class and object

# Example: 1:
class Person:
    # constructor
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    
    def display_person(s):
        print(f"name: { s.name}, age: {s.age}")


p = Person("Abdullah", 25)
p.display_person()
# p.name = "Ali"
# print(p.name)

# Explain:
# class Person: define the class name Person
# __init__ (): constructor method that is called automatically when an object of the class is created. It initializes the attributes of the class.
# self: Refers to the current instance of the class.


# Example: 2

# Add a Method to Change Age in the person class

class Person:
    # constructor
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    
    def display_person(s):
        print(f"name: { s.name}, age: {s.age}")

    def change_age(s):
        s.age += 1

p = Person("abdullah", 25)
p.display_person()
p.change_age()
p.display_person()

