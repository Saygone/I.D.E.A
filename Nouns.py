import random

with open("Nouns.txt", "r") as file:
    data1 = file.read()
    words1 = data1.split()

    word_pos = random.randint(0, len(words1) - 1)
