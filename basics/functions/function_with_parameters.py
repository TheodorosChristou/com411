def climb_ladder(NoR,NoC): #Defines the user function with two parameters
  if (NoR > NoC): #Checks if the number of steps remaining is bigger that steps crossed
    print ("We still have a way to go!")
  else:
    print ("We are almost there")

climb_ladder(5, 2) #Calls the function with 2 parameters
climb_ladder(2, 5)
