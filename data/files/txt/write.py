def search(filename):
  print ("Searching...")
  sections = []
  books = []
  with open(filename) as file:
    for line in file:
      if(line.startswith("Section")):
        linex = line.split(":")
        sections.append(linex[1].replace('\n',''))
      else:
        linex = line.split(":")
        books.append(line.replace('\n',''))
  
  print ("Done!")
 
  return (sections, books)

def save(filename, datatosave):
  print ("Saving...")
  with open(filename, "w") as file:
    print ("Section:{}" .format(datatosave[0]))
    print ("Books:{}" .format(datatosave[1]))
  print ("Done!")

def run():
  data = search("data/files/txt/books.txt")
  save ("data/files/txt/books.txt", data)

run()