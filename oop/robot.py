class Robot:

  MAX_ENERGY = 100 

  # A class attribute
  laws = "Protect, Obey and Survive"

  # A class method
  def the_laws():
    print(Robot.laws)

  # An initialiser (special instance method)
  def __init__(self): # You can provide a name by doing name = "Robot" and change self.name = name

    # An instance attribute
    self.name = "Robot"
    self.age = 0
    self.energy = Robot.MAX_ENERGY

  # An instance method
  def display(self):
    print(f"I am {self.name}")
  
  def __repr__(self):
   return f'robot(name={self.name}, age={self.age}. energy ={self.energy})'

  def __str__(self):
   return f'My name is {self.name} and I am {self.age} years old.'

if (__name__ == "__main__"):
  robot = Robot()
  robot.display()
  print(robot)
  print(repr(robot))