def find_max_between_two_num(num1, num2):
  if num1 > num2:
    return num1
  return num2

# while True:

  # num1 , num2 = map(int, (input("Enter two number: ").split(" ")))
  # res = find_max_between_two_num(num1, num2)
  # print(res)


def find_max_between_three_num(num1, num2, num3):
    if num1 > num2 and num1 > num3:
      return num1
    elif num2 > num1 and num2 > num3:
      return num2
    else:
      return num3

while True:

  num1 , num2 , num3 = map(int, (input("Enter three number: ").split(" ")))
  res = find_max_between_three_num(num1, num2, num3)
  print(f"Maximum number is : {res}")
  
  choice = input("Do you want to continue? (Yes/No): ").strip().lower()
  if choice != "yes":
    print("Exiting the progrm. Goodbye!")
    break
