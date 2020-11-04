def search(namefile):
  print ("Searching...")
  data = {}
  with open(namefile) as file:
    section_name = ""
    for line in file:
      if (line.startswith("Section")):
        linex = line.split(":")
        section_name = linex[1].strip()
      else:
        if (section_name in data):
          value = data[section_name]
          value.append(line.strip())
        else:
          data[section_name] = [line.strip()]
  print ("Done!")
  return data

def run():
  data = search("data/files/txt/books1.txt")
  with open("data/files/txt/generate.csv", "w") as file:

    for item in data.items():
      section = item[0]
      books = item[1]
      for book in books:
        file.write(f"{section},{book}\n")
      
run()
