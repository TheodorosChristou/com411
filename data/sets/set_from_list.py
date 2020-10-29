def observed():
  observations = []
  for count in range (0,7,1):
    print ("Please enter an observation:")
    observation = input()
    observations.append(observation)
  return observations

def run():
  print ("Counting observations...")
  observations = observed()
  observations_set = set()
  for observation in observations:
    observations_set.add((observation, observations.count(observation)))
  print (observations_set)
  for data in observations_set:
   print(f"{data[0]} observed {data[1]} times.")


run()
