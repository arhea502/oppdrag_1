def minFunksjon1():
    print("Dette er en funksjon")
    print("123")

minFunksjon1()


def minFunksjon2(navn):
    print("Hei " + navn)

mittNavn = input("Hva heter du? ")
minFunksjon2(mittNavn)


def squareNumber():
    squareTall1 = int(input("Velg et tall som jeg skal gange med: "))
    squareTall2 = int(input("Velg det andre tallet jeg skal gange med: "))
    print("svaret for", squareTall1, "*", squareTall2, "er:", squareTall1 * squareTall2)

squareNumber()


def minFunksjon3():
    minTekst = "dette er en funksjon!"
    return minTekst

resultat = minFunksjon3()