print ("Enter the first number") #Asks for first number
n1 = int(input())
print ("Enter the second number") #Asks for second number
n2 = int(input())
print ("Enter the third number") #Asks for third number
n3 = int(input())
Odd = 0 #Calculates the number of odds
Even = 0 #Calculates the number of evens
if (n1 % 2 == 0): #Checks if number 1 is even or odd
  Even = Even + 1
else:
  Odd = Odd +1
if (n2 % 2 == 0): #Checks if number 2 is even or odd
  Even = Even + 1 
else:
  Odd = Odd +1
if (n3 % 2 == 0): #Checks if number 3 is even or odd
  Even = Even + 1
else:
  Odd = Odd +1
print ("There were", Even ,"even numbers and", Odd ,"odd numbers")