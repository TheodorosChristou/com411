import matplotlib.pyplot as plt

def read_data(filename):
  temperature_data= []

  with open (filename) as file:
    for line in file:
      temperature = float(line.strip())
      temperature_data.append(temperature)

  return temperature_data


def run():
  data = read_data("visual/subplots/tempts.txt")
  fig , (ax1, ax2) = plt.subplots(1, 2)
  ax1.plot(range(1, 8), data)
  ax2.bar(range(1, 8), data)
  plt.tight_layout()
  plt.show()

run()