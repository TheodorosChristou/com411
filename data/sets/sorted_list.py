def observed():
  observations = []
  for count in range (0,5,1):
    print ("Please enter an observation:")
    observation = input()
    observations.append(observation)
  return observations

def remove_observations(observations):
  runs = True
  while(runs):
    print ("Do you wish to remove an observation (yes/no)?")
    answer = input()
    if(answer == "yes"):
      print ("What observation do you wish to remove?")
      removal = input()
      observations.remove(removal)
      print ("Done")
    else:
      runs = False

def run():
  observations = observed()
  remove_observations(observations)
  observations_set = set()

  for observation in observations:
    times = observations.count(observation)
    observations_set.add( (observation, times))
  
  for key, value in sorted(observations_set):
    print (f"{key} observed {value} times")

run()

