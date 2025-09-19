operator = input("Velg din regneoperasjon +, -, * eller /: ")


tall1 = int(input("Velg ditt første tall: "))
tall2 = int(input("Velg ditt andre tall: "))



while operator != [+, -, *, /]
    if operator == "+":
        print(tall1, "+", tall2, "=", tall1 + tall2)
        svar1 = tall1 + tall2
    elif operator == "-":
        print(tall1, "-", tall2, "=", tall1 - tall2)
        svar1 = tall1 - tall2
    elif operator == "*":
        print(tall1, "*", tall2, "=", tall1 * tall2)
        svar1 = tall1 * tall2
    elif operator == "/":
        if tall1 or tall2 != 0:
            print(tall1, "/", tall2, "=", tall1 / tall2)
            svar1 = tall1 / tall2
        else:
            print("Tallet kan ikke deles på 0")


tall3 = int(input("Velg ditt første tall: "))
tall4 = int(input("Velg ditt andre tall: "))

if operator == "+":
    print(tall3, "+", tall4, "=", tall3 + tall4)
    svar2 = tall3 + tall4
elif operator == "-":
    print(tall3, "-", tall4, "=", tall3 - tall4)
    svar2 = tall3 - tall4
elif operator == "*":
    print(tall3, "*", tall4, "=", tall3 * tall4)
    svar2 = tall3 * tall4
elif operator == "/":
    if tall3 or tall2 != 0:
        print(tall3, "/", tall4, "=", tall3 / tall4)
        svar2 = tall3 / tall4
    else:
        print("Tallet kan ikke deles på 0")

else:
    print("Ugyldig operasjon valgt.")


print("Nå skal jeg legge sammen de to svarene")
print(svar1, "+", svar2, "=", svar1 + svar2)
    

    