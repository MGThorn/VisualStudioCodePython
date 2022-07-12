def init_board():
    return [[None]*8 for _ in range(8)]

def print_board(squares):
    for row in squares:
        print(row)

def read_fen_string(fen_string, squares):
    translatorDikt = {
        "p":"Pawn",
        "n":"Knight",
        "b":"Bishop",
        "r":"Rook",
        "q":"Queen",
        "k":"King",

    }
    
    current_row = 0
    current_column = 0

    for symbol in fen_string:
        print(symbol)

        if(symbol.isnumeric()):
            for i in range(int(symbol)):
               squares[current_row][current_column] = None
               current_column+=1

        elif(symbol.isalpha()):
            squares[current_row][current_column] = translatorDikt[symbol.lower()]
            current_column+=1

        elif(symbol == "/"):
            current_column=0
            current_row+=1

        elif(symbol.isspace()):
            break

#program start
fen_string ="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
board = init_board()



read_fen_string(fen_string,board)
print_board(board)




    