class Book:
    def programming(self):
        print("Introduction to Python")
        print("Introduction to PHP")

    def math(self):
        print("Introduction to linear ALgebra")
        print("Basic Geometry and Trigonomitry")

    def physics(self):
        print("Physics part - 01")
        print("Physics part - 02")


obj = Book()
obj.programming()
obj.math()
obj.physics()

obj1 = Book()
obj1.math()
obj1.x = 10
obj1.y = 20
print(obj1.y)
# print(obj.x)