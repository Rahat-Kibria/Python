from random import randint
for x in range(1, 6):
    guessingNumber = int(input("Enter a number from 1-5: "))
    randomNumber = randint(1, 5)
    if guessingNumber == randomNumber:
        print("You have won")
    else:
        print("You lost")
        print("The number was: ", randomNumber)