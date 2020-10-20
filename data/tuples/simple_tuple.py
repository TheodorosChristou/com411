def likelihood():
  likelihood = (50, 38, 27, 99, 4)
  return min(likelihood)

def run():
  likelihood2 = likelihood()
  print ("Minimum likelihood of falling: {}%" .format(likelihood2))

run()