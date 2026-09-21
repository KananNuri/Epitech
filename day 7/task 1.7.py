import random
from english_words import get_english_words_set

words = get_english_words_set(["web2"], lower=True)

word = random.choice(list(words))

hidden = ["_"] * len(word)

penalty = 0

print(" ".join(hidden))
print("Penalty:", penalty)

while penalty < 12:

    letter = input("Letter: ").lower()

    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                hidden[i] = letter
    else:
        penalty += 1

    print(" ".join(hidden))
    print("Penalty:", penalty)