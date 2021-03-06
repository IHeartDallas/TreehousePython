# This code could have used a while loop to test the player's guess.   
# Instead, I used the while for the try/except.  I wanted to illustrate an array(no pun intended) of concepts covered by the videos.
##########################

#import random moldule for random.randint 
import random

print('This is the Random Number Game.\nWhat is your name?')
name = input()
print("Hi " + name.capitalize() + ", I am thinking of a number from 15 to 25.\nYou have 5 attempts to guess the random number generated by Python's random.randint!")

random_number = random.randint(15, 25)

#use a for loop to track attempts instead of setting a count variable to zero
#use try/except to validate the number is an integer
#parse the player_guess variable to an int value since the input is a string
for count in range(1,6):
    print('Take a guess at the number.')
    while True:
        try:
            player_guess = int(input())
            break
        except ValueError:
            print('Please enter a number')
            continue

    if player_guess < 15:
      print("Out of range")
    elif player_guess > 25:
      print("Out of range")
    elif player_guess < random_number: 
          print('The number you guessed is too low.')
    elif player_guess > random_number:
          print('The number you guessed is too high.')
    elif player_guess == ' ':
          print('Enter a number')
    else:
          break #Break for the correct guess!

if player_guess == random_number:
          print('You did it ' + name.capitalize() + '! You guessed the number in ' + str(count) + ' guesses!')
else:
          print('Game over!  Random.randint came up with the number: ' + str(random_number))


