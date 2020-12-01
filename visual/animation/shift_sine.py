import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import numpy as np 

fig, ax = plt.subplots()

def animate(frame):
 ax.cla()
 ax.set_xlim(0, 720)
 ax.set_ylim(-1, 1)
 x_values = np.arange(0, 720)
 y_values = np.sin((np.pi / 180) * (x_values + frame))
 ax.plot(x_values, y_values, 'r--')

def run():
  simple_animation = animation.FuncAnimation(fig,animate, frames = 720, interval = 100 )
  plt.show()

run()
