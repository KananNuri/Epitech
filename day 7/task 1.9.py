import random
import argparse
from english_words import get_english_words_set


# Argument
parser = argparse.ArgumentParser()

parser.add_argument("--penalty", type=int, default=12)

args = parser.parse_args()

limit = args.penalty


# Get English words
words = get_english_words_set(["web2"], lower=True)

# Choose random word
word = random.choice(list(words))

# Hide the word
hidden = ["_"] * len(word)

# Start penalty
penalty = 0


print(" ".join(hidden))
print("Penalty:", penalty)
print("Penalty limit:", limit)


while penalty < limit:

    guess = input("Letter or word: ").lower()

    # One letter
    if len(guess) == 1:

        if guess in word:

            for i in range(len(word)):
                if word[i] == guess:
                    hidden[i] = guess

        else:
            penalty += 1

    # Full word
    else:

        if guess == word:
            print("You win!")
            break

        else:
            penalty += 5

    print(" ".join(hidden))
    print("Penalty:", penalty)

    # All letters found
    if "_" not in hidden:
        print("You win!")
        break


# Lose
if penalty >= limit:
    print("You lose!")
    print("The word was:", word)