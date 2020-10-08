print ("How many numbers should I sum up?") #Asks the user for the amount of numbers to sum
sum = 0
numbers = int(input())
i = 0
while (numbers > i): #Creates a loop to calculate all the amount of numbers given
  i = i + 1
  print ("Please enter number {0} out of {1}:" .format(i,numbers))
  number = int (input())
  sum = sum + number
print ("The answer is {}." .format(sum)) #Prints out the final amount