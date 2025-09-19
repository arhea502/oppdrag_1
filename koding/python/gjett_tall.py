import random

tall1 = random.randint(0,10)
tall2 = random.randint(0,10)

print(tall1, tall2)

if tall1 > tall2:
    print("tall1:", tall1, "er størst")
elif tall1 < tall2:
    print("tall2:", tall2, "er størst")
else:
    print("Tallene er like store")

fulltall = tall1 + tall2
print("Summer av de tallene er:", fulltall)

if fulltall >= 10:
    print("Summen av tallene er mer eller lik 10")
