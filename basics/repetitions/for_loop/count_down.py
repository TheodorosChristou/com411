print ("How far are we from the cave?") #Asks user how far away the robots are in steps
distance = int(input())
print ("")
for count in range(distance,0,-1): #Creates a loop for each step,counting down until 0
  print ("{} steps remaining..." .format(distance))
  distance = distance - 1
print ("\nWe have reached the cave!")
  
