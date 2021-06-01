gussing_number = 10
i = 0
while i < 3:
    guess = int(input("Guess "))
    if gussing_number == guess:
        print("Correct guessing, You Won!")
        break
    else:
        print("No! incorrect guessing")
    i = i + 1
else:
    print("You failed!")