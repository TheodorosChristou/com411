print ("What type of cover does the book have?") #Asks the user for a cover type
type = input() 

if (type == "soft"): #Determines if its soft
   print ("\nIs the book perfect-bound?")
   pb = input()

   if (pb == "yes"): #Determines if its perfect bound
       print ("\nSoft cover, perfect bound books are very popular!")
   else:
       print ("\nSoft covers with coils or stitches are great for short books")
else: 
  print ("\nBooks with hard covers can be more expensive!")
