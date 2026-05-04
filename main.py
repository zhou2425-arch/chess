import json
from utils import *
from piece_rule import valid_piece_move

with open("board.json", "r") as f:
    board = json.loads(f.read())


while True:
    print_board(board,unicode=True)
    inp = input("\nSelect piece to move!\n\n>>> ")
    if inp == "qQ":
        break
    piece_start = check_input(inp)
    if not piece_start :
        print("Invalid command")
    row_start = piece_start[0]
    col_start = piece_start[1]
    legal_move = valid_piece_move(col_start,row_start,board)
    if not legal_move : 
        print("Chose a valid piece")
        continue
    print_board(board,col_start = col_start,row_start = row_start,legal_move = legal_move,unicode=True,moves=True)
    inp = input("\nSelect your move\n\n")
    if inp == "qQ":
        break
    piece_end = check_input(inp)
    if not piece_end:
        print("Invalid commnad")
        continue
    row_end = piece_end[0]
    col_end = piece_end[1]
    move = (row_end - row_start, col_end - col_start)
    if not move in legal_move:
        print("\nIllegal move\n")
        continue 


    
    piece_start = board[::-1][row_start][col_start]
    piece_end = board[::-1][row_end][col_end]
     #parsinig 

    board[::-1][row_start][col_start] =" "
    board[::-1][row_end][col_end] = piece_start

