def movements():
  path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
  return path

def run():
  print ("Moving...")
  Use = movements()
  print ("{0} for {1} steps" .format(Use[0],Use[1]))
  print ("{0} for {1} steps" .format(Use[2],Use[3]))
  print ("{0} for {1} steps" .format(Use[4],Use[5]))
  print ("{0} for {1} steps" .format(Use[6],Use[7]))

run()
