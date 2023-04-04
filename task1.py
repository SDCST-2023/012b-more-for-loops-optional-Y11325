#!python3

'''
Create a number guessing game
There is a limit of 10 guesses
The program will ask the user to enter an integer from 1 to 100
The program will then tell the user if the number is too high, too low or correct.
If the number is correct, the program will end
If the 10 guesses are used up, the program will say that the user has lost
'''
import random
print("\n\n<<<==Guess the number==>>>\n--you only have 10 attempts--")
computer = random.randint(1,100)
attempts = 0
for i in range(10):
    user = int(input("\nGuess a number: "))
    attempts += 1
    if user == computer:
        print("The number is correct!!!\n\n")
        break
    elif user < computer:
        print("The number is too low\n\n")
        if attempts == 10:
            print("You lost!")
            break
    elif user > computer:
        print("The number is too high\n\n")
        if attempts == 10:
            print("You lost!")
            break