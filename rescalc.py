res = input("What is your Resistance?")
res1 = "." + res
res2 = ((1 - float(res1)) / 1.6)
res3 = ((1 - float(res1)) * 1000)
print("You will take " + str(res2) + "% less damage than at -60 resistance.")
print("You will take " + str(res3) + " per 1,000 damage dealt by an enemy.")