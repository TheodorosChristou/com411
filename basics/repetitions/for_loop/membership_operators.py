print ("What phrase do you see?") #Asks the user to input what they see
phrase = input()
reverse = ""
print ("\nReversing....\n")
print ("The phrase is: ", end="")
for letter in phrase: #Begins the loop for each letter in the phrase given until it reverses it
  reverse = letter + reverse
print (reverse, end="")
