def directions(): #Creates a function that creates the first list and returns it
  directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
  return directions

def menu(): #Creates a function that creates a loop that takes in the user's choices
  direc = directions()
 
  print("")
  for count in range (0, 4, 1):
    print ("{0}:{1}" .format(count, direc[count]))
  User_r = int(input())
  print ("")
  
  return direc[User_r]

def run(): #Creates a function that calls the list and prints in out
  print ("Working out escape route...\n")
  print ("Please select a direction:")
  route = []
  for count in range (0 , 5, 1):
    droute = menu()
    route.append(droute)
  print ("Escape route: {}" .format(route))

run()


