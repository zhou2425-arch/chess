def valid_piece_move(col_start: int ,
                    row_start:int, 
                    board:list[list]):
    """Checks if the move is valid for a piece on this board , moving from start to end coordinates"""
    
    piece_start = board[::-1][row_start][col_start]
    legal_move = []
    print(piece_start)
    if piece_start == " ":
        print("it is not a piece")
        return False
    

    if piece_start in 'Pp': 
        print("stai giocando con un pedone\n")# regole di pedone
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
                    if not (0 <= row_start+ e[0] <= 7 and 0 <= col_start + e[1] <= 7):
                        continue
                    if board[::-1][row_start+ e[0]][col_start + e[1]] != " " : # se trova un pezzo avversario muove in diagonale
                        legal_move.append(e)    
                        print(col_start + e[0])        
               
    if piece_start in 'Nn':     # cavallo
            print("stai giocando con un cavallo")

            possible_moves = [
            (2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)
            ]
            for i , e in possible_moves:
                if  0 <= row_start + i <= 7 and 0 <= col_start + e <= 7 :
                    move = board[::-1][row_start + i][col_start + e]
                    if move != " " and (move.islower()  == piece_start.islower() ):
                        continue
                    legal_move.append((i,e))


    if piece_start in "RrQq" : # torre e regina e vcontrolla se muove in dritta
        print("stai giocando con una torre o una regina")            
        direction = [(1,0),(-1,0),(0,1),(0,-1)] #direzione in alto basso destra sinistra
        possible_moves = [7 - row_start, row_start , 7 -col_start , col_start]  # numero di quadrati dal torre al confine del board per ogni direzione
        indice = 0
        for d in direction :   #controlla se in ogni direzione è bloccato da un pezzo, nel caso 
            times = 1           # di si contare quanti qudrati può muovere fino al confine
            e = possible_moves[indice]
            while times <= e:
                x = (d[0]* times, d[1] * times) 
                move = board[::-1][row_start + x[0]][col_start + x[1]]
                if move != " " :
                    if move.islower()  != piece_start.islower() :
                        legal_move.append(x)
                    break
                legal_move.append(x)
                times += 1
            indice += 1

    if piece_start in "BbQq" :#Alfiere o regina
        print("stai giocando con un alfire o una regina")

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
        indice = 0
        for d in  direction :
            times = 1
            while times <= possible_moves[indice]:
                x = (d[0]* times, d[1] * times)
                move = board[::-1][row_start + x[0]][col_start +  x[1]]
                if move != " " :
                    if move.islower()  != piece_start.islower() :
                        legal_move.append(x)
                    break
                legal_move.append(x)
                times += 1
            indice += 1
    if piece_start in "Kk":
        possible_moves = [(1,1),(0,1),(-1,1),(1,-1),(0,-1),(-1,-1),(1,0),(-1,0)]
        for i , e in possible_moves:
            if 0 <= row_start + i <= 7 and 0 <= col_start + e <= 7 :
                move = board[::-1][row_start + i][col_start + e] 
                if move != " ":
                    if move.islower() == piece_start.islower():
                        continue
                    legal_move((i,e))
                legal_move.append((i,e))
        
    print(legal_move)
    return legal_move   
     


