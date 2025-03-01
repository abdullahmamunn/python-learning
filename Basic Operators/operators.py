# Arithmetic Operators (Perform mathematical operations)
a,b = 10,3
print(a+b) # 10
print(a-b) # 7
print(a*b) # 30
print(a/b) # 3.33
print(a//b) # 3 Floor Division	
print(a%b) # 1 modulas(Remainder)
print(a**b) # 10^3 or 10*10*10 = 1000











# Comparison Operators (Return True or False)
a, b = 10, 3

print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a<=b)
print(a>=b)

# Output:

# False
# True
# True
# False
# False
# True







# Logical Operators (Used to combine conditions)

# and	Returns True if both conditions are True	(5 > 2 and 10 > 5) → True
print(a>b and b<a)
# or	Returns True if at least one condition is True	(5 > 2 or 10 < 5) → True
print(a>b or a<b)
# not	Reverses the result	not (5 > 2) → False
print(not a>b)













# Assignment Operators (Used to assign values)

# +=	Add & Assign	a += 5 → a = a + 5
a += 10 or a = a + 10

# -=	Subtract & Assign	a -= 5 → a = a - 5
a -= 10 or a = a - 10

# *=	Multiply & Assign	a *= 5 → a = a * 5
a *=10 or a = a * 5

# /=	Divide & Assign	a /= 5 → a = a / 5
a /=10 or a = a/5

# //=	Floor Divide & Assign	a //= 5
a = a//10 or a//=10
# %=	Modulus & Assign	a %= 5
a = a%10 or a%=10
# **=	Exponentiate & Assign	a **= 5
b = 100
b **=2
print(b)



# Membership Operators (in, not in)

numbers = [2,5,6,4,8,1,5]
print(5 in numbers) #True
print('5' in numbers) #False


programming_language = ['Python', 'Java', 'Php', 'C++']

print('Python' in programming_language) 


# Quick Practice
# 1️⃣ Write a Python program that takes two numbers and prints their sum, difference, and product.
# 2️⃣ Use logical operators to check if a number is in the range 10-20.
#  solution:
try:
    num = int(input())
    if num >=10 and num<=20:
      print(f"Yes, {num} is bound of 10 - 20")
    else:
      print(f"{num} not in range 10-20")
      
except ValueError:
    print("Invalid Input Data, Please input a valid ata like integer")
# 3️⃣ Perform bitwise AND, OR, and XOR on two numbers (5 and 3).
# 4️⃣ Use membership operators to check if "Python" is in the list ["Java", "Python", "C++"].