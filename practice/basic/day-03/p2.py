# Input N integers. Determine the average. Print the average with two digit after the decimal point.

n = int(input("Enter lenth your number: "))
num = list(map(int,(input("enter your numbers: ").split())))

if(n != len(num)):
  print(f"Your length {n} and its expected {len(num)}")
else:
  avg = sum(num) / n
  print(f"Average is: {avg:.2f}")
