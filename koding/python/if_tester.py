minalder = 17

if minalder > 18:
    print("Du kan ta lappen")
else:
    print("Du er ikke gammel ok")



tall = 5
if tall > 10:
    print("Stemmer")
elif tall < 5:
    print("Stemmer ikke")
elif tall >= 5:
    print("Stemmer kanskje?")
elif tall == 5:
    print("helt riktig")
else:
    print("Stemmer ikke")


alder = int(input("Hvor gammel er du? "))
if alder <= 12:
    print("Du er barn")
elif alder <= 19:
    print("Du er ungdom")
elif alder <= 59:
    print("Du er Voksen")
else:
    print("Du er gammel")

