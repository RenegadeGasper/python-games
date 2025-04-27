import math 
import random

print("Hello World!")
print("What is your name?")
myName = input()
print("It is good to meet you, " + myName)

number = random.randint(1,20)
print("Well, " + myName + ", I am thinking of a number between 1 to 20.")

for guessNumber in range(6):
    print("Take a guess: ")
    guess = input()
    guess = int(guess)

    if guess > number: 
        print ("Guessed number is too high! Try again")

    if guess < number: 
        print ("Guessed number is too low! Try again")
    if guess == number: 
        break

if guess == number: 
    guessNumber = str(guessNumber + 1)
    print ("Good job, " + myName + "! You guessed my number in " + guessNumber + " guesses!")

if guess != number: 
    number = str(number)
    print ("Nope. The number I was thinking of was " + number + ".") 