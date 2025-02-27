def count_vowel(str):
  vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'} #set of vowels
  count = 0

  for char in str:
    if char in vowels:
      count +=1

  
  return count

    # print(char, end="")

while True:
  str = input("Enter String: ")

  res = count_vowel(str)
  print(res)

