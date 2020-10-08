print ("What level of brightness is required?") #Asks the user to input the level of brightness
brightness = int(input())
level = 0
print ("Adjusting brightness...")
print ("")
for count in range(0,brightness,2): #Cretes a loop to adjust the brightness to the user's input
  level = level + 2
  print ("Beep's brightness level:", "*" * level)
  print ("Bop's brightness level:", "*" * level)
  print ("")
print ("\nAdjustments complete!")