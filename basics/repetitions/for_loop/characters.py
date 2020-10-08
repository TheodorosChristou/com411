print ("What strange markings do you see?") #Asks the user to input the markings
markings = input()
print ("\nIdentifying.....")
print ("")
for count in range (0,len(markings),1): #Creates a loop for each character in the markings
  print ("Index", count, ":",markings[count])
print ("\nDone!") 