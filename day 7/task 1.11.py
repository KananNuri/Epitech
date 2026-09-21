import random
import argparse


# Arguments
parser = argparse.ArgumentParser()

parser.add_argument("--penalty", type=int, default=12)
parser.add_argument("--file", type=str, default="words.txt")

args = parser.parse_args()

limit = args.penalty
file_name = args.file


# Read words from file
with open(file_name, "r") as file:
    words = file.read().splitlines()


# Choose random word
word = random.choice(words)

# Hide the word
hidden = ["_"] * len(word)

# Start penalty
penalty = 0


print(" ".join(hidden))
print("Penalty:", penalty)
print("Penalty limit:", limit)


while penalty < limit:

    guess = input("Letter or word: ").lower()

    if len(guess) == 1:

        if guess in word:

            for i in range(len(word)):
                if word[i] == guess:
                    hidden[i] = guess

        else:
            penalty += 1

    else:

        if guess == word:
            print("You win!")
            break

        else:
            penalty += 5

    print(" ".join(hidden))
    print("Penalty:", penalty)

    if "_" not in hidden:
        print("You win!")
        break


if penalty >= limit:
    print("You lose!")
    print("The word was:", word)