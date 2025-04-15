# Exercise 1: Create a Car Class
# Goal: Define a class called Car with:
# brand and model as attributes
# A method car_info() that prints: "This car is a {brand} {model}"

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def car_info(self):
        print(f"This car is a {self.brand} {self.model}")


c = Car("Toyota", "Corolla")
c.car_info()


# Exercise 2: Add a Speed Method
# Extend the Car class above with:

# A new attribute: speed = 0

# A method accelerate(amount) that increases the speed by amount

# A method get_speed() that prints the current speed

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.speed = 0
    
    def car_info(self):
        print(f"This car is a {self.brand} {self.model}")
    
    def accelerate(self, amount):
        self.speed += amount
    
    def get_speed(self):
        print(f"The current speed is {self.speed} km/h")


c = Car("Toyota", "Corolla")
c.car_info()
c.accelerate(50)
c.get_speed()
c.accelerate(30)
c.get_speed()
c.accelerate(10)
c.get_speed()

# output:

# This car is a Toyota Corolla
# The current speed is 50 km/h
# The current speed is 80 km/h
# The current speed is 90 km/h