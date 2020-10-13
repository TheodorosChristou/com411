def display_ladder(steps): #Defines the new function that will create the ladder
  print ("|   |")
  for steps in range (steps): #Creates the loop for all the steps
    print ("*****")
    print ("|   |")

def create_ladder(): #Defines the new function of asking the steps and also creating the ladder by calling the previous function
  print ("How many steps are left?")
  steps = int(input())
  display_ladder(steps)

create_ladder() #Calls the second function