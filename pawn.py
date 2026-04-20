def valid_pawn_move(col_start: int ,
                    row_start:int,
                     col_end:int,
                     row_end:int, 
                    board:list[list]):
    """Checks if the move is valid for a pawn on this board , moving from start to end coordinates"""
    
    piece_start = board[::-1][row_start][col_start]
    piece_end = board[::-1][row_end][col_end]
    move_end = (row_end,col_end)

    print(piece_start)
   
    if piece_end != " ":

        if piece_start.islower() != piece_end.isupper():
            print("iiii")
            return True
    
    if piece_start in 'Pp':
    
            forward_direction = 1 
            if piece_start == 'p':
                forward_direction = -1
            possible_moves = {
            "forward":(forward_direction,0),
            "dobble": (forward_direction * 2,0),
            "right":(forward_direction, 1),
            "left" :(forward_direction, -1)
            }
            for m in possible_moves:
                distance = possible_moves.get(m)
                possible_moves[m]= (row_start + distance[0],col_start + distance[1])
            piece_end = board[::-1][row_end][col_end]
            for i , e in possible_moves.items():
                match i :
                    case "forward" :
                        if board[::-1][e[0]][e[1]] != " ":
                            possible_moves["forward"] = 0
                    case "dobble":
                        if not (piece_start.islower() and row_start == 6) and not (piece_start.isupper() and row_start == 1):
                            possible_moves["dobble"] = 0
                    case "right" | "left":
                        if board[::-1][e[0]][e[1]] == " " :
                            possible_moves[i] == 0
            move_end = (row_end,col_end)
            if move_end in possible_moves.values():
                 return False                
    elif piece_start in 'Nn':
            direction = 1
            if piece_start == 'n' :
                direction = -1
            possible_moves = [
            (direction*2,1),
            (direction*2,-1),
            (direction*-2,1),
            (direction*-2,-1),
            (direction,2),
            (direction,-2),
            (direction*-1,2),
            (direction*-1,-2),
            ]
            legal_move =[]
            for m in possible_moves:
                legal_move.append((row_start + m[0], col_start + m[1]))
            move_end = (row_end,col_end)
            if move_end in legal_move:
                return False
    elif piece_start in "Rr" :
        if col_start != col_end and row_end != row_start :
            return True 
        possible_moves = [(1,0),(-1,0),(0,1),(0,-1)]
        space = [7 - row_start, row_start , 7 -col_start , col_start]
        legal_move = []
        indice = 0
        for i in possible_moves :
            times = 1
            e = space[indice]
            while times <= e:
                x = (i[0]* times, i[1] * times) 
                legal_move.append((row_start + x[0],col_start + x [1]))
                times += 1
                if board[::-1][row_start + x[0]][col_start + x[1]] != " ":
                    break
            indice += 1
        print(legal_move)


        if move_end in legal_move :

            return False
    
    elif piece_start in "Bb":
        space = [
        min(7- row_start,col_start), #alto sinistra
        min(7 - row_start, 7-col_start), # alto destra
        min(row_start,col_start), # basso sinistra
        min(row_start,7 - col_start)#basso destra
        ]
        direction =[
            (1,-1), 
            (1,1),
            (-1,-1),
            (-1,1)

        ]
        legal_move = []
        for x in  direction :
            times = 1
            indice = 0
            while times <= space[indice]:
                
                legal_move.append((row_start + x[0] * times ,col_start + x[1] * times))
                times += 1
                if board[::-1][row_start + x[0]][col_start + x[1]] != " ":
                    break
            indice += 1
        if move_end in legal_move:
            return False
    elif piece_start in "Qq" :
        
        



        
    
    
    
    return True
        


