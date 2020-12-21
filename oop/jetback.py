from tech import Tech

class Jetpack(Tech):

  def __init__(self):
    super().__init__()

  def __repr__(self):
    return "jetpack()"

  def activate(self):
    print ("Activating Jetpack")

  def deactivate(self):
    print ("Deactivating Jetpack")

  def fly(speed):
    print (f"Flying at speed of {speed}")

if __name__ == "__main__":
  jetpack = Jetpack()
  print(repr(jetpack))
  Jetpack.fly(50)