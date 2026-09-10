text = input("Text: ")
key = int(input("Key: "))
result = ""

for letter in text.lower():
    if letter == " ":
          result += " "     
    else:
      result += chr((ord(letter) - 97 + key) % 26 + 97)

print(result)