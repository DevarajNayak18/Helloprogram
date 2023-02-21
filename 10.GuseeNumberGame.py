#This is the Guess number game
import random  #import random library
print("what is your name?")
name=input()
secretNumber=random.randint(1,10)
print("well,"+ name + ',im thinking the number btw 1 and 10')
#ask to the player to guess the number within 2 times
for guess in range(1,3):
    print("take a guess")
    guess=int(input())
    if guess>secretNumber:
        print("your guess is too high")
    elif guess<secretNumber:
        print("your guess is too low")
    else:
        break
if guess==secretNumber:
    print("good job, the guess number ," +str(guess) + " is correct")
else:
    print("nope, the guess number ," +str(guess )+ "incorrect")
