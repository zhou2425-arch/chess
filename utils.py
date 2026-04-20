import json

fen_start = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
fen_start_simbol = "♜♞♝♛♚♝♞♜/♟♟♟♟♟♟♟♟/8/8/8/8/♙♙♙♙♙♙♙♙/♖♘♗♕♔♗♘♖"

UNICODE_PIECES = {
    "K": "♔",
    "Q": "♕",
    "R": "♖",
    "B": "♗",
    "N": "♘",
    "P": "♙",
    "k": "♚",
    "q": "♛",
    "r": "♜",
    "b": "♝",
    "n": "♞",
    "p": "♟",
    " ": " ",
}

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

def print_board(board, unicode=False):
    if unicode:
        board_copy =[]
        row = []
        for line in board:
            for element in line:
                row.append(element)
            board_copy.append(row)
            row = []
        for row in board_copy:
            for i,e in enumerate(row):
                if e != ' ':
                    row[i] = UNICODE_PIECES.get(e)
    print("\n  +---+---+---+---+---+---+---+---+")
    for i, row in enumerate(board_copy):
        rank = 8 - i
        print(f"{rank} | " + " | ".join(row) + " |")
        print("  +---+---+---+---+---+---+---+---+")
    print("    a   b   c   d   e   f   g   h\n")





board = fen2matrix(fen_start)
with open("board.json", "w") as f:
    f.write(json.dumps(board))
