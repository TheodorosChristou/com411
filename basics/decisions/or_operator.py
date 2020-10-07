print ("What type of adventure should I have?")
adventure_type = input()
if ((adventure_type == "short") or (adventure_type == "scary")):
  print ("\nEntering the dark forest!")
elif ((adventure_type == "safe") or (adventure_type == "long")):
  print ("\nTaking the safe route!")
else:
  print ("\nNot sure which route to take.")
