def search(filename):
  print ("Searching...")
  with open(filename) as file:
    lines  = file.read().split('\n')
    for line in lines:
      print(f"looked in {line}.")
  print ("...Done!")

def run():
 search("data/files/txt/locations.txt")

run()



  