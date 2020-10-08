print ("How many numbers should I sum up?")
sum = 0
numbers = int(input())
i = 0
while (numbers > i):
  i = i + 1
  print ("Please enter number {0} out of {1}:" .format(i,numbers))
  number = int (input())
  sum = sum + number
print ("The answer is {}." .format(sum))