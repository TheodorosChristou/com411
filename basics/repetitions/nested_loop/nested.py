print ("How many rows should I have?") #Asks user to input the amount of desired rows
rows = int(input())
print ("\nHow many columns should I have?") #Asks user to input the amount of desired columns
columns = int(input())
print ("Here I go\n")
for count in range (0,rows,1): #Creates a loop for the amount of rows given
  for count in range (0,columns,1): #Creates a second loop for the amount of colums given
    print (":-)", end="")
  print("") 