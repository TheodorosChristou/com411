def search(filename):
  print ("Searching...")
  with open(filename) as file:
    for line in file:
      print(f"looked in {line}")
  print ("Done")

def run():
  location = search("data/files/txt/locations.txt")
  search2 = search(location)
  print(search2)

run()



  