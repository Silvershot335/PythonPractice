import math

# Fuel required to launch a given module is based on its mass. 
# Specifically, to find the fuel required for a module, 
# take its mass, divide by three, round down, and subtract 2.

def calc_fuel(mass):
  m3 = (int(mass) / 3)
  rd = math.trunc(m3)
  fuel = rd - 2
  return fuel

total = 0

with open("input.txt", "r") as work:
    lines = work.read().split()

    for mass in lines:
      fuel = calc_fuel(mass) 
      total += fuel
      print(f'{mass}: {fuel}')
    
    print(total)