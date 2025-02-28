# Problem_2:
# You will be given an input N, You have to print the sum of all odd integers between 1 to N.
# If N=6 then the corresponding output is: 1+3+5=9


def sum_of_odd_numbers(n):
    sum = 0
    for i in range(1, n + 1):
        if i % 2 == 1:  # Check if the number is odd
            print(i)  # Print the odd number
            sum = sum + i
    return sum


while True:
    n = int(input("Enter a number: "))
    res = sum_of_odd_numbers(n)
    print(f"Sum is {res}")  # Use 'res' to print the result

