class Father:
     def fatherMother(self):
         print("I am your Father")
         super().fatherMother()


class Mother:
    def fatherMother(self):
        print("I am you Mother")


class Child(Father, Mother):
    pass



ch = Child()
ch.fatherMother()