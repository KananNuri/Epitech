n = int(input("Number: "))
text = input("Text: ")
if n == 0:
    quit()
if any(v in text.lower() for v in "aeiou"):
    print(n)
elif n >= 42:
    print(n)
else:
    print(text)