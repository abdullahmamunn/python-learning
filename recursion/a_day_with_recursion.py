# Print i to n
def PrintNum(i,n):
    # Base Case
    if i>n:
        return 1
    # Recursive Case
    else:
        print(i)
        PrintNum(i+1,n)


# Find Factorial
def Factorial(n):
    # Base Case
     if n<=1:
         return 1
     # Recursive Case
     else:
         return n * Factorial(n-1)


# print Febonacci serise
def Febonacci(n):
    # Base Case
    if n == 1:
        return 1
    if n == 2:
        return 1
   # Recursive Case
    return  Febonacci(n-1) + Febonacci(n-2)




print("Choose Your Option:")
print("___Press 1 for PrintNumbers___")
print("___Press 2 for Factorial___")
print("___Press 3 for Febonanacci___")

while True:
    x = int(input("Enter your choose: "))
    if x == 1:
        i = int(input())
        n = int(input())
        PrintNum(i, n)  # print numbers
    elif x == 2:
        fact = int(input())
        print(Factorial(fact))  # Print Factorials
    elif x == 3:
        febo = int(input())
        print(Febonacci(febo))
    else:
        print("Invalid Option")

# Palindrome




