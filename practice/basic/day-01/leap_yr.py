def find_leap_year(year):
  if (year %4 == 0 and year %100 != 0) or (year %400 == 0):
    print(f"{year} is Leap Year")
  else:
    print(f"{year} is not Leap Year")


while True:
  year = int(input("Enter a Year: "))
  find_leap_year(year)

  str = input("want to continue? (yes/no): ").strip().lower()

  if str == "no":
    print("Goodbye")
    break


