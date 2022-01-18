# A guessing game
import random
num=random.randint(1,10)
chance = 0
while chance < 5:
    chance = chance + 1
    print("Guess a number between 1 and 10")
    guess=int(input("Enter your guess: "))
    if guess == num:
        print("You guessed right")
        break
    elif guess < num:
        print("Try higher")
    elif guess > num:
        print("Try lower")
if not chance < 5:
    print("You lose. The number was ", num)