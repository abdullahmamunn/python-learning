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

    """
    Guess 9
    No! incorrect guessing
    Guess 20
    No! incorrect guessing
    Guess 12
    No! incorrect guessing
    You failed!
    
    Process finished with exit code 0
    
    Guess 10
    Correct guessing, You Won!

    """