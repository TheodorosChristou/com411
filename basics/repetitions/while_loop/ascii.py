print ("How many bars should be charged?") #Asks the user for the amount of bars
bars = int(input())
bars_charged = 0
while (bars > bars_charged):
  bars_charged = bars_charged + 1
  print ("Charging:","█" * bars_charged)
print ("\nThe battery is fully charged.")
