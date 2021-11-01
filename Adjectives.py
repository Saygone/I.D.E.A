import random

with open("Adjectives.txt", "r") as file:
    data = file.read()
    words = data.split()

    word_pos = random.randint(0, len(words) - 1)


