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
