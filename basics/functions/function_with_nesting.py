def identify(): #Defines the new function
  print ("What lies before us?") #Asks for what the robots see ahead
  see = str(input())
  if (see == "a large boulder"): #Checks for the nested decision
    print ("\nIts time to run!")
  else:
    print ("\nWe will be fine")

identify() #Calls the function