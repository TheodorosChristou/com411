print ("What do I hear?") #Asks the user to indentify what Beeb heard
hear = input()
if (hear == "muffled steps"):
  print ("\nWhat do I see around me?")
  see = input()
  if ((see == "wolf") or (see == "giant spider")):
    print ("What defensive protocol should I initiate? (shouting,flamethrower,scary face)")
    defensive_protocol = input()
    if ((defensive_protocol == "shouting") or (defensive_protocol == "flamethrower")):
      print ("The creature got afraid and ran away,I can keep going!")
    else:
        print ("Defensive Protocol did not work! Initiating running!")
  elif ((see == "squirrel" ) or (see == "rabbit")):
    print ("\nIts an adorable animal,what are some ways to safetly approach it? (two suggestions)")
    approach1 = input()
    approach2 = input()
    if ((approach1 == "walk slowly") and (approach2 == "calm sounds")):
      print ("Approached the animal succesfully and had a fun time playing around! Time to keep going!")
    else:
      print ("Approach was not succesful,time to keep going!")
  else:
    print ("I dont understand so I will keep going!")
else:
  print ("I dont understand so I will keep going!")
