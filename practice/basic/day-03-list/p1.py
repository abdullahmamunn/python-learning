# Take an input N. In the next line input N integers. Print this N integers in separate lines.


n = int(input("Enter lenth your number: "))
num = list(map(int,(input("enter your numbers: ").split())))

if(n != len(num)):
  print(f"Your length {n} and its expected {len(num)}")
else:
  for nm in num:
    print(nm)

