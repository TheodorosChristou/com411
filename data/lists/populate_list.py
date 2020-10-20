def directions(): #Creates a function that creates the first list and returns it
  directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
  return directions

def menu(): #Creates a function that creates a loop that takes in the user's choices
  print ("Please select a direction: ")
  direc = directions()
  User_res = []
  print ("Please select a direction")
  for count in range(0 , 5, 1):
    print("")
    for count in range(0 , 4, 1):
      print ("{0}:{1}" .format(count, direc[count]))
    
    User_r = int(input())
    User_res.append(direc[User_r])
  print ("")
  
  return User_res

def run(): #Creates a function that calls the list and prints in out
  print ("Working out escape route...")
  route = menu()
  print ("Escape route {}" .format(route))

run()


