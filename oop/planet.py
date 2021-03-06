from human import Human
from robot import Robot

class Planet:
  
  def __init__(self):
    self.humans = []
    self.robots = []

  def __repr__(self):
    return f"planet(humans = {self.humans}, robots= {self.robots}"

  def __str__(self):
    return f"This planet has {len(self.humans)} humans and {len(self.robots)} robots."

  def add_human(self, human):
    self.humans.append(human)

  def add_robot(self, robot):
    self.robots.append(robot)

  def remove_human(self, human):
    self.humans.remove(human)

  def reove_robot(self, robot):
    self.robots.remove(robot)

if (__name__ == "__main__"):
  planet = Planet()
  print(repr(planet))
  planet.add_human("Theo")
  print(repr(planet))
  print(planet)