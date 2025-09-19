

navn = input("Hva heter du? ")
alder = int(input("Hvor gammel er du? "))
tall = int(input("Gi et tall "))
ganging = int(0)

print("Hei " + navn)

if alder > 18:
    print("Du er myndig")
else:
    print("Du er ikke myndig")

for i in range(10):
    ganging = ganging + 1
    print(ganging, "x 3 =", tall * ganging)




