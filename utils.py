import json

fen_start = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
fen_start_simbol = "♜♞♝♛♚♝♞♜/♟♟♟♟♟♟♟♟/8/8/8/8/♙♙♙♙♙♙♙♙/♖♘♗♕♔♗♘♖"


def fen2matrix(fen):
    def row2list(row):
        l = []

        for c in row:
            if c.isdigit():
                l += [" "] * int(c)
            else:
                l.append(c)

        return l

    board = []

    for row in fen.split("/"):
        board.append(row2list(row))

    return board


def matrix2fen(board):
    def row2str(row):
        f = ""
        spaces = 0

        for c in row:
            if c == " ":
                spaces += 1
            else:
                if spaces > 0:
                    f += str(spaces)
                    spaces = 0
                f += c

        if spaces > 0:
            f += str(spaces)
            spaces = 0

        return f

    fen = ""
    for row in board:
        fen += row2str(row) + "/"

    return fen[:-1]


def show_board(
    board: list[list],
):  # : list[list] serve per dire al compilatore che tipo di oggetto è board
    n = 8
    for riga in board:
        print("   +---+---+---+---+---+---+---+---+")
        print(n, end="  ")
        n -= 1
        for elemento in riga:
            print("|", end=" ")
            print(elemento, end=" ")
        print("|")
    print("")
    print("     a   b   c   d   e   f   g   h   ")


board = fen2matrix(fen_start)
with open("board.json", "w") as f:
    f.write(json.dumps(board))
