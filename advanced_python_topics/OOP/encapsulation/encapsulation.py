def encapsulation_example():
    class Person:
        def __init__(self, name, age, salary=0):
            self.name = name          # public attribute
            self._age = age           # “protected” attribute (by convention)
            self.__salary = salary    # private attribute (name‑mangled to _Person__salary)

        def get_salary(self):
            return self.__salary      # public getter for the private salary

        def set_age(self, age):
            if age > 0:
                self._age = age
            else:
                print("Age must be positive.")

    person = Person("Alice", 30, salary=50000)
    # Accessing salary via the getter:
    print(person.get_salary())   # 50000

    # Protected attribute (by convention—accessible but “internal”):
    print(person._age)           # 30

    # Update age correctly:
    person.set_age(35)
    print(person._age)           # 35

    # Attempt invalid age:
    person.set_age(-5)           # prints "Age must be positive."

    # Trying to access the private salary directly will fail:
    try:
        print(person.__salary)
    except AttributeError:
        print("Cannot access __salary directly!")  # This will run

    # But Python name‑mangles it, so this works (not recommended):
    print(person._Person__salary)  # 50000

# Run the example
encapsulation_example()
