print ("What do I hear?") #Asks the user to indentify what Beeb hears
hear = input()
if (hear == "muffled steps"):
  print ("\nWhat do I see around me?") #Asks the user to indentify what Beeb sees
  see = input()
  if ((see == "wolf") or (see == "giant spider")): #Determines if what Beeb saw is dangerous
    print ("What defensive protocol should I initiate? (shouting,flamethrower,scary face)")
    defensive_protocol = input()
    if ((defensive_protocol == "shouting") or (defensive_protocol == "flamethrower")): #Determines if the defensive protocol is effective
      print ("The creature got afraid and ran away,I can keep going!")
    else:
        print ("Defensive Protocol did not work! Initiating running!")
  elif ((see == "squirrel" ) or (see == "rabbit")): #Determines if what Beeb saw is safe to approach
    print ("\nIts an adorable animal,what are some ways to safetly approach it? (two suggestions)")
    approach1 = input()
    approach2 = input()
    if ((approach1 == "walk slowly") and (approach2 == "calm sounds")): #Determines if Beeb's approach was succesful 
      print ("Approached the animal succesfully and had a fun time playing around! Time to keep going!")
    else:
      print ("Approach was not succesful,time to keep going!")
  else:
    print ("I dont understand so I will keep going!")
else:
  print ("I dont understand so I will keep going!")
