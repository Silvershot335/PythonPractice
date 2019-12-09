import math

with open("input.txt", "r") as work:
    x = work.read().split()
    print(x)

    for y in x:
        print("yo")

        z = (int(y) / 3)

        print(math.trunc(z))

        c = (int(math.trunc(z)) - 2)

        print(c)

        with open("output.txt", "a") as output:
        
           output.write(str(c))
           output.write(",")

with open("output.txt", "r") as work:
    d = work.read().split(",")
    print(d)

    t = 0
    for number in d:
      if number != "":
          t =  (t + int(number))
print(t)
      
        
