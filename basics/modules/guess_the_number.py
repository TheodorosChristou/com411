import random as rnd # We implement the random module function to generate a random number for the program
print ("Please enter the minimum value:") #We get the minimum and maximum range of the random guess
min = int(input())
print ("Please enter the maximum value:")
max = int(input())
print ("I am thinking a number between {0} and {1}. Can you guess what is it?" .format(min,max))
number = rnd.randrange(min, max + 1, 1) #We Activate the random module with the given range 
answer = int(input())
while (number != answer): #While the answer is not the random number we go through a loop of the guessing game,giving hints until the correct number is found
  if (answer <= number - 3):
    print ("Your answer is too low")
  elif (answer >= number + 3):
    print ("Your answer is too high")
  print ("Try again:")
  answer = int(input())

print ("Congratulations! You guessed my number!")
