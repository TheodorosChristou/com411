print ("What phrase do you see?")
phrase = input()
reverse = ""
print ("\nReversing....\n")
print ("The phrase is: ", end="")
for letter in phrase:
  reverse = letter + reverse
print (reverse, end="")
