print ("Program Started!")
print ("Please enter a letter:") #Asks for a letter
letter = input()
if (len(letter) == 1): #Checks if the user put the correct input
  print ("The ASCII code for",letter,"is: {}" .format(ord(letter))) #Transforms the letter into its ascii code and prints it
else:
  print ("Invalid input!")
print ("Program Ended!")