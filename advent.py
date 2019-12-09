import math


math.floor(1.2)
1

math.floor(-0.5)
-1


def round_down(n, decimals=0):
    multiplier = 1 ** decimals
    return math.floor(n * multiplier) / multiplier


with open("input.txt", "r") as work:
    x = work.read().split()
    print(x)

    for y in x:
        print("yo")

        z = (int(y) / 3)

        print(round_down(z))

        c = (int(z) - 2)

        print(c)

        
