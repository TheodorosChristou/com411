print ("What type of adventure should I have?") #Asks the user what type of adventure Beeb should have 
adventure_type = input()
if ((adventure_type == "short") or (adventure_type == "scary")): #Determines if its short or scary
  print ("\nEntering the dark forest!")
elif ((adventure_type == "safe") or (adventure_type == "long")): #Determines if its safe or long
  print ("\nTaking the safe route!")
else:
  print ("\nNot sure which route to take.")
