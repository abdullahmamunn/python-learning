# Exercise 1: Person → Student
# Parent: Person with attributes name, age, and method introduce() that prints "I’m {name}, {age} years old."
# Child: Student adds grade attribute and method study() that prints "{name} is studying in grade {grade}."




# Exercise 2: Vehicle → Car & Motorcycle
# Parent: Vehicle with brand and method start() printing "{brand} engine started."

# Child:

# Car adds num_doors and overrides start() to also print "Car doors: {num_doors}"

# Motorcycle adds has_sidecar and overrides start() accordingly.







# Exercise 3: Account → SavingsAccount
# Parent: BankAccount with owner, balance, and basic deposit()/withdraw()

# Child: SavingsAccount adds interest_rate and method apply_interest() that increases balance by balance * interest_rate/100







# Exercise 4: Animal Hierarchy (Multi-Level Inheritance)
# Level 1: Animal with name, method eat()

# Level 2: Mammal(Animal) adds hair_color and method nurse_young()

# Level 3: Dog(Mammal) adds breed and method bark() — test that a Dog can still call eat() and nurse_young()







# Exercise 5: Shape → Rectangle & Square
# Parent: Shape with abstract methods area() and perimeter() (you can just raise NotImplementedError)

# Children:

# Rectangle(width, height) implements both methods

# Square(side) inherits from Rectangle (hint: call super().__init__(side, side))