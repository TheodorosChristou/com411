def search(filename):
  print ("Searching..." , end="")
  sections = []
  books = []
  with open(filename) as file:
    for line in file:
      if(line.startswith("Section")):
        linex = line.split(":")
        sections.append(linex[1].replace('\n',''))
      else:
        books.append(line.replace('\n',''))
  
  print ("Done!")
 
  return (sections, books)

def save(filename, datatosave):
  print ("Saving..." , end="")
  with open((filename), "w") as file:
    file.write("Section: ")
    for index in range(len(datatosave[0])):
      if (index < len(datatosave[0]) - 1):
       file.write(f"{datatosave[0][index]},")
      else:
        file.write(f"{datatosave[0][index]}")
    
    file.write("\n")

    file.write("Books: ")
    for index in range(len(datatosave[1])):
      if (index < len(datatosave[1]) - 1):
       file.write(f"{datatosave[1][index]},")
      else:
        file.write(f"{datatosave[1][index]}")
  print ("Done!")

def run():
  data = search("data/files/txt/books.txt")
  save ("data/files/txt/books.txt", data)

run()