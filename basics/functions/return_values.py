def sum_weight(bop_weight, beeb_weight):
  sum = bop_weight + beeb_weight
  return sum

def calc_avg_weight(bop_weight, beeb_weight):
  avg = sum_weight(bop_weight, beeb_weight) / 2
  return avg 

def run():
  print ("What is the weight of Beep?\n")
  Bweight = int(input())
  print ("What is the weight of Bop?\n")
  Boweight = int(input())
  print ("What would you like to calculate (sum or average)?\n")
  calculate = input()
  if (calculate == "sum"):
    answer = sum_weight(Boweight, Bweight)
    print ("The sum of Beep's and Bop's weight is {}." .format(answer))
  elif (calculate == "average"):
    answer = calc_avg_weight(Boweight, Bweight)
    print ("The average of Beep's and Bop's weight is {}." .format(answer))
  else:
    print ("Action not recognised")

run()



