while True:
    num1 = int(input("Enter your First number: "))
    num2 = int(input("Enter your Second number: "))
    num3 = int(input("Enter your Third number: "))
    if num1 < num2 and num1 < num3:
        print("{0} is Small".format(num1))
    elif num2 < num1 and num2 < num3:
        print("{0} is Small".format(num2))
    else:
        print("{0} is small".format(num3))

