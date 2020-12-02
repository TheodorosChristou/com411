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

if (__name__ == "__main__"):
  robot = Robot()
  robot.display()
