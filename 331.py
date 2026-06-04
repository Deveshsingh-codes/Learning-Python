 # Python task 
 # 1.---- GUESS THE NUMBER ----
 
from numbers import Number


n = 134
print("Number of guesses is limited to only 9 times")
Number_of_guesses = 0
while(Number_of_guesses<=9):
    guess = int(input("Guess the number: "))
    if guess<n:
        print("You entered a smaller number, try again!")
    elif guess>n:
        print("You entered a greater number, try again!")
    else:
        print("Congratulations! You guessed the number in ", Number_of_guesses, "guesses")
        break
    Number_of_guesses+=1
if(Number_of_guesses>9):
    print("Game over")
        
        
    