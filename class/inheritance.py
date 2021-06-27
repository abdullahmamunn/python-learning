class Parent:
    def assets(self):
        print("10 gold coins")
    home = 4


class ChildOne(Parent):
    pass


class ChildTwo(Parent):
    pass

    def earns(self):
        print("2 gold coins")


ch1 = ChildOne()
ch1.assets()
print(ch1.home)

ch2 = ChildTwo()
ch2.assets()
print(ch2.home)
ch2.earns()