import json
from utils import show_board
from pawn import valid_pawn_move
from print_board import print_board

with open("board.json", "r") as f:
    board = json.loads(f.read())

col = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}

while True:
    # 1. show board
    print_board(board,unicode=True)

    # 2. get user input move
    move = input("\nPlay your move!\n\n>>> ")
       

    # 2.1 parse user input (dividere un input in sottoclassi)
    move_start, move_end = move[:2], move[-2:]
    col_start = move_start[0].lower()
    row_start = move_start[-1]
    if move.lower() == "q":

        break
    if len(move) != 4 :
        print("Invalid move")
        continue
    
    if col_start not in "abcdefgh":
        print("Invalid move")
        continue
    
    if row_start not in "12345678":
        print("Invalid move")
        continue
        
    col_end = move_start[0].lower()
    row_end = move_start[-1]

    if col_end not in "abcdefgh":
        print("Invalid move")
        continue
    
    if row_end not in "12345678":
        print("Invalid move")
        continue
    col_start = int(col.get(move_start[0]))    
    row_start = int(move_start[-1]) - 1

    col_end = int(col.get(move_end[0]))
    row_end = int(move_end[-1]) - 1
    if valid_pawn_move(col_start,row_start,col_end,row_end,board):
        print("\nIllegal move\n")

        continue


    
    piece_start = board[::-1][row_start][col_start]
    piece_end = board[::-1][row_end][col_end]
     #parsinig 

    if piece_start !=" ":
         board[::-1][row_start][col_start] =" "
         board[::-1][row_end][col_end] = piece_start

