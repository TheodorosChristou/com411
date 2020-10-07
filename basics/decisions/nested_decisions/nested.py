print ("What type of cover does the book have?")
type = input()

if (type == "soft"):
   print ("\nIs the book perfect-bound?")
   pb = input()

   if (pb == "yes"):
       print ("\nSoft cover, perfect bound books are very popular!")
   else:
       print ("\nSoft covers with coils or stitches are great for short books")
else:
  print ("\nBooks with hard covers can be more expensive!")
