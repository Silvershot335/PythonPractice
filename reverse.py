txt = input()
back = txt [::-1]

print(back)

if back.casefold() == txt.casefold():
    print("Palindrome!")