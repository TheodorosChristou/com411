print("What is your name human?") #Asks user for their name.
name = input()
print("How old are you?(in years)") #Asks user for their age.
age = int(input())
print("How tall are you(in meters)?") #Asks user for their height.
height = float(input())
print("How much do you weight(in kilograms)?") #Asks user for their weight.
weight = float(input())
bmi = float(weight / height ** 2) #Calculates bim based on weight and height.
bmif = '{0:.4g}'.format(bmi) #Keeps only 2 decimals
print(name,"you are",age,"years old and your bmi is {}.".format(bmif))