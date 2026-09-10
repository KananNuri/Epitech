import math

alphabet = "abcdefghijklmnopqrstuvwxyz"

freq = [
    8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015,
    6.094, 6.966, 0.153, 0.772, 4.025, 2.406,
    6.749, 7.507, 1.929, 0.095, 5.987, 6.327,
    9.056, 2.758, 0.978, 2.360, 0.150, 1.974, 0.074
]

text = input("Encrypted text: ").lower()
key_length = int(input("Key length: "))

letters = [c for c in text if c in alphabet]
shifts = []
key = ""

for k in range(key_length):
    column = letters[k::key_length]

    shift = max(
        range(26),
        key=lambda s: sum(
            math.log(freq[(alphabet.index(c) - s) % 26])
            for c in column
        )
    )

    shifts.append(shift)
    key += alphabet[shift]

result = ""
j = 0

for c in text:
    if c in alphabet:
        result += alphabet[(alphabet.index(c) - shifts[j % key_length]) % 26]
        j += 1
    else:
        result += c

print("Key:", key)
print("Decrypted:", result)