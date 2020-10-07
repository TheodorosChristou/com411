print ("Where should I look?") #Asks the user for a location to look
l = input()
if (l == "in the bedroom"): #Determines if the location is the bedroom
  print ("Where in the bedroom should I look?")
  lb = input()
  if (lb == "under the bed"):
    print ("Found some shoes but no battery")
  else:
      print ("Found some mess but no battery.")
elif (l == "in the bathroom"): #Determines if the location is the bathroom
  print ("Where in the bathroom should I look?")
  lb2 = input()
  if (lb2 == "in the bathtub"):
    print ("Found a rubber duck but no battery")
  else:
     print ("Found a wet surface but no battery.")
elif (l == "in the lab"): #Determines if the location is the lab
  print ("Where in the lab should I look?")
  lb3 = input()
  if (lb3 == "on the table"):
    print ("Yes! I found my battery!")
  else:
     print ("Found some tools but no battery.")
else:
    print("I dont know where that is but I will keep looking.")


