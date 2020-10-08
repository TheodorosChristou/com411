print ("What phrase do you see? (In reverse)") #Asks the user to answer what phrase Beeb sees
phrase = input()
r_phrase = 0
print ("\nReversing......\n")
print ("The phrase is: ", end="")
for position in range (len(phrase)-1,-1,-1): #Creates a loop to reverse the phrase
  print (phrase[position], end="")


 
 