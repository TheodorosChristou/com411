def cwd():
  import os
  path = os.getcwd()
  print ("The current working folder is {}" .format(path))
  print ("The folder contains the following:")
  for file in os.listdir(path):
    print (file)

def run():
  print ("Processing...")
  fileprint = cwd()
  print (fileprint)

run()