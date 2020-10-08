print ("Please enter a number:") #Asks the user for a number
number = int(input())
i = 0
sum = 1
while (number > i): #Creates a loop to calculate the factorial for a number
  i = i + 1
  sum = sum * i
print ("The factorial is {}." .format(sum))
