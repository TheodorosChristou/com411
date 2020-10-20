def likelihood(): #Defines a function that creates the tuple list and returns the min and max
  likelihoods = (50, 38, 27, 99, 4)
  return min(likelihoods), max(likelihoods)

def run(): #Defines a function that prints out the returned min and max
  likelihoods2 = likelihood()
  print ("Minimum likelihood of falling: {}%" .format(likelihoods2[0]))
  print ("Maximum likelihood of falling: {}%" .format(likelihoods2[1]))

run()