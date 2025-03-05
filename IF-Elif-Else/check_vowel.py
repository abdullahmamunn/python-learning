'''
This program is identify whether a number is vowel or consonant
'''
while True:
 char = input("Enter a English alphabet: ")
 if char == 'a' or char == 'A' or char == 'e' or char == 'E' or char == 'i' or char == 'I' or char == 'o' or char == 'O' or char == 'u' or char == 'U':
    print("{0} is vowel".format(char))
 else:
    print("{0} is consonant".format(char))
