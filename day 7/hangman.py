import random
import argparse
import time


# Arguments
parser = argparse.ArgumentParser()

parser.add_argument("--penalty", type=int, default=12)
parser.add_argument("--length", type=int, default=0)
parser.add_argument("--file", type=str, default="words.txt")
parser.add_argument("--time", type=int, default=60)

args = parser.parse_args()

limit = args.penalty
word_length = args.length
file_name = args.file
time_limit = args.time


# Read words from file
with open(file_name, "r") as file:
    words = [word.strip().lower() for word in file if word.strip()]


# Filter words by length
if word_length > 0:
    words = [word for word in words if len(word) == word_length]


# Check if words exist
if len(words) == 0:
    print("No words found!")
    exit()


# Choose random word
word = random.choice(words)

# Hide word
hidden = ["_"] * len(word)

# Start values
penalty = 0
won = False
time_over = False

start_time = time.time()


print("HANGMAN")
print(" ".join(hidden))
print("Penalty:", penalty)
print("Penalty limit:", limit)


while penalty < limit:

    # Check time
    passed_time = time.time() - start_time

    if passed_time >= time_limit:
        time_over = True
        break

    guess = input("Letter or word: ").strip().lower()

    # Check time again after input
    passed_time = time.time() - start_time

    if passed_time >= time_limit:
        time_over = True
        break

    # Empty input
    if guess == "":
        continue

    # Player writes one letter
    if len(guess) == 1:

        if guess in word:

            for i in range(len(word)):

                if word[i] == guess:
                    hidden[i] = guess

        else:
            penalty += 1

    # Player writes full word
    else:

        if guess == word:
            won = True
            break

        else:
            penalty += 5


    print(" ".join(hidden))
    print("Penalty:", penalty)


    # Check if all letters are found
    if "_" not in hidden:
        won = True
        break


# Final result
if won:
    print("You win!")
    print("The word was:", word)

elif time_over:
    print("Time is over!")
    print("You lose!")
    print("The word was:", word)

else:
    print("You lose!")
    print("The word was:", word)