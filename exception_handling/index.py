try:
    age = int(input("Your age : "))
    print(age)
except ValueError:
    print("Invalid input, your age have to be a number")

try:
    num = int(input("enter a number: "))
    income = 2000
    cost = income / num
    print(cost)
except ZeroDivisionError:
    print("you can't divide by zero")
