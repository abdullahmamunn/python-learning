# This program will convert your weight
weight = int(input("Your weight: "))
unit = input("(L)bs or (K)g: ")
if unit.upper() == "L":
    converted = 0.45 * weight
    print("Your weight is {0} kilos".format(converted))
else:
    converted = weight / 0.45
    print("Your weight is {0} pounds".format(converted))