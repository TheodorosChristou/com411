print ("Please enter the first number") #Asks user for the first number
n1 = int(input())
print ("Please enter the second number") #Asks user for the second number
n2 = int(input())
if (n1 > n2): #Determines if the first number is bigger
  print ("\nThe second number is smallest")
elif (n1 < n2): #Determines if the second number is bigger
  print ("\nThe first number is smallest")
else: #Comes to the conclusion that both are equal
  print ("\nBoth are equal!")