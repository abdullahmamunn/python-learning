# 1. Value error
try:
    print("For ValueError")
    age = int(input("Your age : "))
    print(f"your age is {age}")
    if age < 0:
        raise ValueError("age can't be negative")
    if age > 120:
        raise ValueError("age can't be greater than 120")
    print("age is valid")
except ValueError as e:
    print(f"Invalid input, your age have to be a number {e}")
except TypeError:
    print("Invalid input, ")
except Exception as e:
    print(f"Invalid input, your age have to be a number {e}")
finally:
    print("end")




try:
    print()
    print("For ZeroDivisionError")
    num = int(input("enter a number: "))
    print("print cost")
    income = 2000
    cost = income / num
    print(cost)
except ZeroDivisionError:
    print("you can't divide by zero")
finally:
    print("end")
