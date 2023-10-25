import random

with open("./hyakunin.txt", Encoding="utf-8") as f:
    wakas = [s.strip() for s in f.readlines()]

print(wakas[random.randrange(len(wakas))])
