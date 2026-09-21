import sys
import random
import pygame
from datetime import date


# -------------------------
# WORD FILE
# -------------------------

if len(sys.argv) < 2:
    print("Error: missing argument", file=sys.stderr)
    sys.exit(1)

filename = sys.argv[1]

try:
    with open(filename, "r") as file:
        words = []

        for line in file:
            word = line.strip().lower()

            if word and word.isalpha():
                words.append(word)

except FileNotFoundError:
    print("Error: file not found", file=sys.stderr)
    sys.exit(1)


if not words:
    print("Error: empty word list", file=sys.stderr)
    sys.exit(1)


# -------------------------
# GAME DATA
# -------------------------

word = random.choice(words)

guessed_letters = []
attempts = 0


# -------------------------
# PYGAME
# -------------------------

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman")

font = pygame.font.Font(None, 50)
small_font = pygame.font.Font(None, 32)

running = True
game_over = False


# -------------------------
# GAME LOOP
# -------------------------

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and not game_over:

            letter = event.unicode.lower()

            if letter.isalpha() and len(letter) == 1:

                if letter not in guessed_letters:
                    guessed_letters.append(letter)
                    attempts += 1


    # -------------------------
    # HIDDEN WORD
    # -------------------------

    hidden_word = ""

    for letter in word:

        if letter in guessed_letters:
            hidden_word += letter + " "
        else:
            hidden_word += "_ "


    # -------------------------
    # CHECK WIN
    # -------------------------

    won = True

    for letter in word:

        if letter not in guessed_letters:
            won = False


    if won:
        game_over = True


    # -------------------------
    # DRAW SCREEN
    # -------------------------

    screen.fill("white")

    title = font.render("HANGMAN", True, "black")
    screen.blit(title, (300, 50))

    word_text = font.render(hidden_word, True, "black")
    screen.blit(word_text, (200, 250))

    attempts_text = small_font.render(
        f"Attempts: {attempts}",
        True,
        "black"
    )

    screen.blit(attempts_text, (20, 20))

    guessed_text = small_font.render(
        "Letters: " + " ".join(guessed_letters),
        True,
        "black"
    )

    screen.blit(guessed_text, (20, 550))


    if game_over:

        win_text = font.render(
            f"You found {word}!",
            True,
            "green"
        )

        screen.blit(win_text, (250, 350))


    pygame.display.flip()


pygame.quit()


# -------------------------
# HIGH SCORE
# -------------------------

if game_over:

    score_file = "highscores.txt"
    today = date.today()

    best_score = None
    best_date = None

    try:

        with open(score_file, "r") as file:

            for line in file:

                try:
                    score, score_date = line.strip().split(",")
                    score = int(score)

                    if best_score is None or score < best_score:
                        best_score = score
                        best_date = score_date

                except ValueError:
                    continue

    except FileNotFoundError:
        pass


    if best_score is None or attempts < best_score:

        with open(score_file, "a") as file:
            file.write(f"{attempts},{today}\n")

        print(
            f"Best ever! You guessed "
            f"'{word}' in {attempts} attempts."
        )

    else:

        print(
            f"You guessed '{word}' in {attempts} attempts, "
            f"but the record from {best_date} "
            f"is {best_score} attempts."
        )