# The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.

# In python we mainly see two flavor
    # 1. Method overriding (via inheritance
    # 2. Duck typing ( no inheritance required)


# Example

class Animal:
    def speak(self):
        print("Animal makes a sound.")

class Dog(Animal):
    def speak(self):               # Overrides parent
        print("Dog says Woof!")

class Cat(Animal):
    def speak(self):               # Overrides parent
        print("Cat says Meow!")

# We can treat all as Animal...
def make_animal_speak(animal: Animal):
    animal.speak()

make_animal_speak(Dog())   
make_animal_speak(Cat())  
make_animal_speak(Animal())  
# make_animal_speak("Dog")  # TypeError: 'str' object is not callable

# output
# Dog says Woof!
# Cat says Meow!
# Animal makes a sound.



# Duck Typing


class Bird:
    def fly(self):
        print("Bird can fly")


class Airplane:
    def fly(self):
        print("Airplane can fly!")


def let_it_fly(fliable):
    fliable.fly()


let_it_fly(Bird())
let_it_fly(Airplane())
