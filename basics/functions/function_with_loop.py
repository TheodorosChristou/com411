def cross_bridge(distance): #Defines the function for the bridge
  for count in range (0,distance,1): #Creates a loop to count the steps
    print ("Crossed step")
  if (distance >= 5): #Determines if the steps are more than 5
    print ("The bridge is collapsing!")
  else:
    print ("we must keep going!")

cross_bridge(3) #Calls the function with parameters
cross_bridge(6)
  