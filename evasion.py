er = input("Enter your Evasion Rating:")
dc = input("Enter your Dodge Chance:")
dc1 = "." + dc
ec = (584 * 1.15) / (584 + ((float(er) * .25) ** .8))
print(ec)
cp1 = (1 - ec)
cp2 = 1 - float(dc1)
cpa = 1 - (cp1 * cp2)
print("Your chance to prevent attacks is " "{:.2%}".format(cpa) + ".")
