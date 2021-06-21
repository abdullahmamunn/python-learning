class Student:
    dept = "Computer Science and Engineering"

    # constructor with parameter
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def learning(self):
        # print("Your name is:",self.name, "And id:",self.id)
        print("Your name is:", self.name)
        print("Id: ", self.id)
        print("department: ", self.dept)

    def show(self,name):
        print("My name is", name)


stu = Student("Abdullah Al Mamun", 184)
stu.learning()
stu.show("Mamun")