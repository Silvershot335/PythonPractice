with open('namesforjudah.txt', 'r') as a:
    print(a.read())

with open('namesforjudah.txt', 'a') as b:


    if 'new' in input():
        print("Enter New Nickname") 
        b.write(input("")+", ")
 
with open('namesforjudah.txt', 'r') as c:

    print(c.read())