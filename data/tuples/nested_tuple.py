def steps(): #Defines the function that creates the list of steps and their value
  likelihoods = []
  likelihoods.append(("step 1", 50))
  likelihoods.append(("step 2", 38))
  likelihoods.append(("step 3", 27))
  likelihoods.append(("step 4", 99))
  likelihoods.append(("step 4", 99))
  return likelihoods

def run(): #Defines the function that calls the previous list and creates two more to count how many steps are above 50 and adds them to their representive list and prints them at the end
  likelihoods2 = steps()
  good_steps = []
  bad_steps = []
  for likelihood in likelihoods2:
    if(likelihood[1] >= 50):
      bad_steps.append(likelihood)
    else:
      good_steps.append(likelihood)
  print ("Good steps: {0}, Bad steps: {1}" .format(len(good_steps),len(bad_steps)))

run()


    
