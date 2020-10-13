print ("Program started!")
print ("Please enter an ASCII code")
number = abs(int(input()))

if (number >= 32 and number <= 126):
  ascii_character = chr(number)
  print ("The character represented by the ASCII code {} is {}".format(number, ascii_character))
else:
    print ("Invalid number!")

print ("Program Ended!")
  