# Problem_1:
# You will be given an input N, You have to print all integers between 1 to N in reversed order.
# If N=5 then the corresponding output is: 5 4 3 2 1

def decrease_nth_to_one(n):
  for i in range(n, 0, -1): #range(start, stop, step)
    print(i, end=" ")

decrease_nth_to_one(10)
