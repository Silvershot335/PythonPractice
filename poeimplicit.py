import math
attempts = input("How many attempts?")
implicit = input("How many implicits?")

#a =
#b =
#c =

print(implicit, ",",  attempts)

d = (.25 ** int(implicit))
#print(d)
c = (int(attempts) - int(implicit))
#print(c)
e = (.75 ** int(c))
#print(e)

a = (d * e)

#print(a)

fx = math.factorial(int(attempts))
fj = math.factorial(int(implicit))
fxj = math.factorial(int(attempts) - int(implicit))

#print(fxj)
#print(fx)
#print(fj)

b = (fx) / (fj * fxj)

print(a * b)
