import matplotlib.pyplot as plt

def coordinate():
  print ("please enter the x value")
  x = input()
  print ("please enter the y value")
  y = input()
  x_y_values= (x, y)
  return x_y_values

def path():
  print ("Retrieving path...")
  x_value = []
  y_value = []
  for index in range(4):
    data = coordinate()
    x_value.append(data[0])
    y_value.append(data[1])
  return x_value, y_value

def run():
  values = path()
  x = values[0]
  y = values[1]
  plt.plot(x, y, 'ro--')
  plt.show()

run()