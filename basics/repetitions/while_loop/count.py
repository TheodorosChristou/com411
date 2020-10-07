print ("How many live cables must I avoid?") #Asks the user for the amount of live cables to avoid
cables_avoid = int(input())
cables_avoided = 0 #Counts all the cables avoided
while (cables_avoid > cables_avoided): #Creates a loop until all live cables have been avoided
  print ("Avoiding...", end="")
  cables_avoided = cables_avoided + 1
  print ("...Done! {} live cables avoided!" .format(cables_avoided))
print ("\nAll live cables have been avoided.")
