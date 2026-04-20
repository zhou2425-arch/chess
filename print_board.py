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