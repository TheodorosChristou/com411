import matplotlib.pyplot as plt #Imports the matplotlib 

def display(x,y): #Defines a function that creates the plot
  plt.plot(x, y)
  plt.show()

def run(): #Defines a function that gets the values and calls the first function
  x_values = [1, 2, 3, 4, 5]
  y_values = [1, 4, 9, 16, 25]
  display(x_values,y_values)

run()