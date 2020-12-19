from tech import Tech

class Laser(Tech):

  MAX_RANGE = 100

  def __init__(self):
    super().__init__()

  def __repr__(self):
    return "laser()"

  def activate(self):
    print ("Activating laser")

  def deactivate(self):
    print ("Deactivating laser")

  def range(range, distance):
    if (distance > Laser.MAX_RANGE):
      print(f"Fired maximum range of {Laser.MAX_RANGE}")
    else:
      print(f"Fired a distance of {distance}")


if __name__ == "__main__":
  laser = Laser()
  print(repr(laser))
  laser.range(50)
  laser.range(150)