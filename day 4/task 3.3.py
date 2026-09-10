text = input("Text: ").lower()
key = input("Key: ").lower()
mode = input("e/d: ")
result = ""
j = 0

for letter in text:
    if letter not in "abcdefghijklmnopqrstuvwxyz":
        result += letter
        continue

    shift = ord(key[j % len(key)]) - 97

    if mode == "e":
        result += chr((ord(letter) - 97 + shift) % 26 + 97)
    else:
        result += chr((ord(letter) - 97 - shift) % 26 + 97)

    j += 1

print(result)