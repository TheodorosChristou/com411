print ("Please enter a phrase:") #Asks the user to enter a phrase
phrase = str(input())
i = 0
while (len(phrase) > i): #Creates a loop to count all the characters
  i = i + 1
print ("Bob " * i)