def listen(): #Defines the new function
  print ("What sound did I just hear?") #Asks the user for the sound
  sound = str(input())
  print ("\nThat was a loud {}!" .format(sound))

listen() #Excecutes the function

