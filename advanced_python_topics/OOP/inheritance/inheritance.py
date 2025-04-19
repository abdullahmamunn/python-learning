# Example of inheritances

# Single Inheritance
# Defination: ekta child class ekta single Parent class k inherit korle seta k bole single inheritance 
# child class cayle tar parent class er methods and attribute overrode kore use korte pare

# Example 01
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes sounds"

class Dog(Animal):
#    pass
   def speak(self): #here override methods
        return f"{self.name} makes sounds Woo wooo"
        

dog = Dog("Tom")
print(dog.speak())


# Example 02
# self
# It is always the first parameter of instance methods in a class.
# self allows methods to access the instance's attributes and other methods.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def intro(self):
        return f"Hi, I am {self.name} and I am {self.age} years old"


class Teacher(Person):
    def __init__(self, name, age, dept):
        super().__init__(name, age)
        self.dept = dept
    
    def intro(self):
        return f"{super().intro()} and My department is {self.dept}"


class Student(Person):
    def __init__(self, name, age, dept, student_id):
        super().__init__(name, age)
        self.dept = dept
        self.student_id = student_id

    def intro(self):
        return f"{super().intro()} and My department is {self.dept} and student_id is {self.student_id}"


t = Teacher("Abdullah", 25, "Engineering and Life Science")

t2 = Teacher("Fahmida", 20, "Earth and Enviornmental Science")
print(t.intro())
print(t2.intro())

s = Student("Abdullah", 25, "Engineering and Life Science", "184")
s2 = Student("Fahmida", 20, "Earth and Enviornmental Science", "185")
print(s.intro())
print(s2.intro())


# Example of Multilevel Inheritance
# Definition : ekta parent class k ekta child class inherit korle parent calss er sob attribute child e ase amra jani,
# ekhon another grand_child jodi child class k inherti kore then se both child class ar parent class er sob 
# property pacche

# Example 01

# Parent Class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

# Child Class (inherits from Animal)
class Mammal(Animal):
    def feed(self):
        return f"{self.name} feeds its young with milk."

# Grandchild Class (inherits from Mammal)
class Dog(Mammal):
    def speak(self):
        return f"{self.name} barks."

# Create an object of the Grandchild class
dog = Dog("Buddy")
print(dog.speak())      # Output: Buddy barks
print(dog.feed())       # Output: Buddy feeds its young with milk


# Example 02

# Base Class
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def move(self):
        return f"The {self.brand} vehicle is moving."

# Intermediate Class
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)  # Calling parent constructor
        self.model = model

    def car_info(self):
        return f"This is a {self.brand} {self.model}."

# Derived Class
class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity

    def charge(self):
        return f"The {self.brand} {self.model} is charging with {self.battery_capacity} kWh capacity."

# Create an object of the ElectricCar class
tesla = ElectricCar("Tesla", "Model S", 100)
print(tesla.move())          # Output: The Tesla vehicle is moving.
print(tesla.car_info())      # Output: This is a Tesla Model S.
print(tesla.charge())        # Output: The Tesla Model S is charging with 100 kWh capacity.



# Example of Multiple Inheritance

# Definition: Multiple Inheritance holo ekta child class doi ba tar beshi class k inherit kore
# Key Features:
# A single class inherits from two or more parent classes.
# The derived class has access to all the attributes and methods of its parent classes.
# Useful for combining different functionalities in a single class.


# Example 01:

# Parent Class 1
class Engine:
    def start(self):
        return "Engine started."

    def stop(self):
        return "Engine stopped."

# Parent Class 2
class Wheels:
    def roll(self):
        return "Wheels are rolling."

# Child Class (inherits from both Engine and Wheels)
class Car(Engine, Wheels):
    def drive(self):
        return "Car is driving."

# Create an object of the Car class
my_car = Car()
print(my_car.start())  # Output: Engine started.
print(my_car.roll())   # Output: Wheels are rolling.
print(my_car.drive())  # Output: Car is driving.


# Example :2

# Parent Class 1
class Mother:
    def skills(self):
        return "Good at cooking."

# Parent Class 2
class Father:
    def skills(self):
        return "Good at carpentry."

# Child Class (inherits from both Mother and Father)
class Child(Mother, Father):
    def skills(self):
        # Combine skills from both parents
        return f"{super(Mother, self).skills()} and {super(Father, self).skills()}."

# Create an object of the Child class
child = Child()
print(child.skills())  # Output: Good at cooking and Good at carpentry.






























class Parent:
    def assets(self):
        gold = 4
        return gold



class ChildOne(Parent):
    pass


class ChildTwo(Parent):
    pass

    def earns(self):
        c_t = 4 + self.assets()
        return c_t


ch1 = ChildOne()
c1 = ch1.assets()
# print(f"Child one got asset from his father {c1} gold")

ch2 = ChildTwo()
c2 = ch2.assets()

c2_e = ch2.earns()

# print(f"Child two got asset from his father {c2} gold and he earn golds also Total he has now {c2_e}")




