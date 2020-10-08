print ("How many mountains should I display?") #Asks the user how many mountains to display
mountains = int(input())
print ("Displaying....")
for count in range(mountains): #Creates a loop to display the amount of mountains given
  print ("""
           __
          /  \\_  
         /^    \\
        /  ^    \\_
      _/ ^ ^     ^\\
     /  ^     ^    \\


     """)

print ("Done!")