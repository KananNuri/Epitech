import random
import argparse
import time


# Arguments
parser = argparse.ArgumentParser()

parser.add_argument("--penalty", type=int, default=12)
parser.add_argument("--file", type=str, default="words.txt")
parser.add_argument("--time", type=int, default=60)

args = parser.parse_args()

limit = args.penalty
file_name = args.file
time_limit = args.time


# Read words from file
with open(file_name, "r") as file:
    words = file.read().splitlines()


# Choose random word
word = random.choice(words)

hidden = ["_"] * len(word)

penalty = 0

# Start timer
start_time = time.time()


print(" ".join(hidden))
print("Penalty:", penalty)
print("Time limit:", time_limit, "seconds")


while penalty < limit:

    # Calculate time
    passed_time = time.time() - start_time

    if passed_time >= time_limit:
        print("Time is over!")
        print("The word was:", word)
        break

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