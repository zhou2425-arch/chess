def valid_piece_move(col_start: int ,
                    row_start:int,
                     col_end:int,
                     row_end:int, 
                    board:list[list]):
    """Checks if the move is valid for a piece on this board , moving from start to end coordinates"""
    
    piece_start = board[::-1][row_start][col_start]
    piece_end = board[::-1][row_end][col_end]
    move = (row_end - row_start ,col_end - col_start) # per dopo contrallare se si trova nel legal move
    legal_move = []





    print(piece_start)
   
    if piece_end != " ":                                # Controlla se il piece_end è un pezzo
        
        if piece_start.islower() != piece_end.isupper():#Contreollla se il pezzo è avversario
        
            return False                                 # True = no valid move, False = valid move
    
    if piece_start in 'Pp':                              # regole di pedone
    
            direction = 1 
            if piece_start == 'p':                       #se è un pedone nero , un passo avanti vuol
                direction = -1                           # dire numero di riga -1
            possible_moves = {
            "forward":(direction,0),
            "dobble": (direction * 2,0),
            "right":(direction, 1),
            "left" :(direction, -1)
            }
            for key , e in possible_moves.items():

                match key :
                    case "forward" :
                        if board[::-1][row_start + e[0]][col_start + e[1]] == " ":  #se è vuoto aggiunge qusto indice a lgal move
                            legal_move.append(e)
                    case "dobble":
                        if ((piece_start.islower() and row_start == 6) or (piece_start.isupper() and row_start == 1)) and board[::-1][row_start + e[0]][col_start + e[1]] == " ": # se è la prima mossa e il destinario è vuoto
                            legal_move.append(e)
                    case "right" | "left":
                        if board[::-1][e[0]][e[1]] != " " :                         # se trova un pezzo avversario muove in diagonale
                            legal_move.append(e)            
               
    elif piece_start in 'Nn':     # cavallo
            
           
            legal_move = [
            (2,1),
            (2,-1),
            (-2,1),
            (-2,-1),
            (1,2),
            (1,-2),
            (-1,2),
            (-1,-2),
            ]


    elif piece_start in "Rr" : # torre
        if col_start != col_end and row_end != row_start : # controlla se muove in dritta
            return False 
        direction = [(1,0),(-1,0),(0,1),(0,-1)] #direzione in alto basso destra sinistra
        possible_moves = [7 - row_start, row_start , 7 -col_start , col_start]  # numero di quadrati dal torre al confine del board per ogni direzione
        indice = 0
        for d in direction :   #controlla se in ogni direzione è bloccato da un pezzo, nel caso 
            times = 1           # di si contare quanti qudrati può muovere fino al blocco
            e = possible_moves[indice]
            while times <= e:
                x = (d[0]* times, d[1] * times) 
                legal_move.append(x)
                times += 1
                if board[::-1][row_start + x[0]][col_start + x[1]] != " ":
                    break
            indice += 1

    elif piece_start in "Bb": #Alfiere
        if abs(row_start - row_end) != abs(col_end - col_start):
            return False
        possible_moves = [
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
        for x in  direction :
            times = 1
            indice = 0
            while times <= possible_moves[indice]:
                
                legal_move.append((x[0] * times, x[1] * times))
                times += 1
                if board[::-1][row_start + x[0]][col_start + x[1]] != " ":
                    break
            indice += 1
    print(legal_move)
    print(move)
    return move in legal_move        


