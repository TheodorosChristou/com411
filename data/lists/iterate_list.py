def directions(): #Creates a function that creates the first list and returns it
  directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
  return directions

def menu(): #Creates a second function that calls the list and creates the loop to create the desired message
  print ("Please select a direction:")
  direc = directions()
  for index in range(len(direc)):
    print ("{0}:{1}" .format(index, direc[index]))
    
    


def run(): #Calls the second loop to print out the desired message
  menu()

run()

