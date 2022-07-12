translatorDikt = {
    "p":"Pawn",
    "n":"Knight",
    "b":"Bishop",
    "r":"Rook",
    "q":"Queen",
    "k":"King",

}
FenString ="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
i = 0

for Symbol in FenString:
    if(Symbol.isnumeric):
        print("Zahl")
    elif(Symbol.isalpha):
        print("Buchstabe")
    