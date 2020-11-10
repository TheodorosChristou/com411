import matplotlib.pyplot as plt
import random as rnd

def data():
  paths = {}
  print("What type of line (:,-- or-)?")
  linetype = input()
  print ("What color (r,g or b)?")
  color = input()
  print("What type of marker(o,s or ^)?")
  markerstyle = input()
  paths['linetype'] = linetype
  paths['color'] = color
  paths['markerstyle'] = markerstyle
  return paths

def generate():
  print ("How many lines would you like to display?")
  numberlines = int(input())
  for numberline in range(numberlines):
    values = data()
    x = [0, rnd.randrange(1, 10)]
    y = [0, rnd.randrange(1, 10)]
    plt.plot(x, y, f"{values['color']}{values['linetype']}{values['markerstyle']}")

def run():
  print ("Running...")
  generate()
  plt.show()
  print ("Done!!")

run()




