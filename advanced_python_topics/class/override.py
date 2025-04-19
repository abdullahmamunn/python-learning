class Monster:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def attack(self):
        print('I am attacking...')


class Fogthing(Monster):
    def attack(self):              # Overrides parent
        print('I am killing...')

    def make_sound(self):
        print('Grrrrrrrrrr\n')


class Shooting(Monster):
    def attack(self):
        print("I am Shooting...")

    def sound(self):
        print("Greeeeeeeee..")

fogthing = Fogthing("Fogthing", "Yellow")
fogthing.attack()
fogthing.make_sound()

sh = Shooting("Mamun", "Red")
print(sh.name)
print(sh.color)
sh.attack()
sh.sound()