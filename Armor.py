armor = input("What is your armor value?")
dr = (int(armor) / (int(armor) + (10 * 1000)))
print("You will reduce "+ "{:.0%}".format(dr) + (" of a 1,000 damage hit."))