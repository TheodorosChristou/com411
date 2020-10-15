def box(word): #Displays the word in a box
  num_length =4 + len(word)
  print ("-" * num_length)
  print ("| {} |" .format(word))
  print ("-" * num_length)

def lowcase(word): #Displays the word in lower case
  print (word.lower())

def uppercase(word): #Displays the word in upper case
  print (word.upper())

def displaymirrored(word): #Mirrors the word
    mirrored = ""
    for letter in reversed(word):
        mirrored += letter
    print ("{} | {}".format(word, mirrored))

def repeat(word): #Repeats the word, changing between lower and upper based on the number
  print ("How many times do you want to repeat it?")
  repeat = int(input())
  for repetition in range(repeat):
    if (repeat % 2 == 0):
      print (word.lower())
    else:
      print (word.upper())

def run(): #Runs the program
  print ("Please enter a word")
  word = input()
  response = 0
  while (response != 6):
        print("What would you like to do with this word?")
        print("[1] Display in a box")
        print("[2] Display lower-case")
        print("[3] Display upper-case")
        print("[4] Display mirrored")
        print("[5] Display repeated")
        print("[6] Quit")

        response = int(input())

        if (response == 1):
          box(word)
        elif (response == 2):
          lowcase(word)
        elif (response == 3):
          uppercase(word)
        elif (response == 4):
          displaymirrored(word)
        elif (response == 5):
          repeat(word)
        elif (response == 6):
          break
        else:
          print ("Unknown option")

run ()
        