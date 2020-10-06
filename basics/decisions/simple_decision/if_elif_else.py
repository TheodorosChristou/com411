print ("Towards which direction should I paint (up,down,left,right?") # Asks user for a direction to paint
direction = input()
if (direction == "up"): #Confirmes which message to send based on the direction given
  print ("\nI'm painting in the upward direction!")
elif (direction == "down"):
  print ("\nI'm painting in the downward direction!")
elif (direction == "left"):
  print ("\nI'm painting in the leftward direction!")
elif (direction == "right"):
  print ("\nI'm painting in the rightward direction!")
else:
  print("\nUnknown direction to paint")