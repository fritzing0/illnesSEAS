#This is a comment
#Pyhton doesn't read
#what does here.
#Only for Humans

#prints hello world
#print("Hello, World!")
#print(answer, "inspires you!")
#i=-1
#while True:
#    i+= 1
#
#    if(i > 20):
#        break
#
#        # i is odd
#    if (i % 2 !=0):
#            continue
#
#    print(i)
#imports the ability to get a random number (we will learn more about this later!)
#from random import *

#Generates a random integer.
#imports the ability to get a random number (we will learn more about this later!)
#from random import *
#Generates a random integer.
aRandomNumber = random.randint(1, 20)
# For Testing: print(aRandomNumber)
guessesTaken = 0
while guessesTaken < 3:
    print("take a guess")
    guess = input()
    guess = int(guess)
    guessesTaken = guesseTaken + 1
guess = input("Guess a number between 1 and 20 (inclusive): ")
if not guess.isnumeric(): # checks if a string is only digits 0 to 9
    print("That's not a positive whole number, try again!")
else:
	guess = int(guess) # converts a string to an integer
    if aRandomNumber < guess:
        print("guess higher")
        guessesTaken +1
    if aRandomNumber > guess:
        print("guess lower")
        guessesTaken + 1
    if aRandomNumber == guess:
        print("yay. you guessed correct")
        break
