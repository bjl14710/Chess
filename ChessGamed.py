class Chess:
    def __init__(self):
        #8x8
        '''
        1 = pawn
        2 = knight
        3 = rook
        4 = bishop
        5 = Queen
        6 = King
        '''
        self.board = [
                      [[3,"red",0],[2,"red",0],[4,"red",0],[6,"red",0],[5,"red",0],[4,"red",1],[2,"red",1],[3,"red",1]],
                      [[1,"red",0],[1,"red",1],[1,"red",2],[1,"red",3],[1,"red",4],[1,"red",5],[1,"red",6],[1,"red",7]],
                      [[0,"",0],[0,"",0],[0,"",0],[0,"",0],[0,"",0],[0,"",0],[0,"",0],[0,"",0]],
                      [[0,"",0],[0,"",0],[0,"",0],[0,"",0],[0,"",0],[0,"",0],[0,"",0],[0,"",0]],
                      [[0,"",0],[0,"",0],[0,"",0],[0,"",0],[0,"",0],[0,"",0],[0,"",0],[0,"",0]],
                      [[0,"",0],[0,"",0],[0,"",0],[0,"",0],[0,"",0],[0,"",0],[0,"",0],[0,"",0]],
                      [[1,"black",0],[1,"black",1],[1,"black",2],[1,"black",3],[1,"black",4],[1,"black",5],[1,"black",6],[1,"black",7]],
                      [[3,"black",0],[2,"black",0],[4,"black",0],[6,"black",0],[5,"black",0],[4,"black",1],[2,"black",1],[3,"black",1]]
                      ] 
        # select the type
        self.Type = {"pawn":1, "knight":2, "rook":3, "bishop":4, "Queen":5, "King":6}
        self.rows = 8
        self.cols = 8

    def findPiece(self,piece,color,number):
        for r in range(self.rows):
            for c in range(self.cols):
                FoundPiece = (self.board[r][c][0] == self.Type[piece] 
                              and self.board[r][c][1] == color
                              and self.board[r][c][2]  == number)
                if FoundPiece:
                    return [r,c]
        return [-1,-1]

    def movePawn(self, select, move, color) -> bool:
        # determine specific pawn.
        ROWS, COLS = len(self.board), len(self.board[0])
        red_directions = {"forward": (1,0), "back": (-1,0), "left":(0,-1),"right":(1,0)}
        black_directions = {"forward": (-1,0), "back": (1,0), "left":(0,1),"right":(-1,0)}
        r,c = self.findPiece("pawn",color,select)
        print(r,c)
        if r == -1 and c == -1:
            print("piece not found")
            return 
        if color == "black":
            # use black_directions
            dr,dc = black_directions[move]
            Row = r + dr
            Col = c + dc
        elif color == "red":
            dr, dc = red_directions[move]
            Row = r + dr
            Col = c + dc
            # use red directions
        else:
            print("not found")
            return
        # make the move
        if (Row not in range(ROWS) or 
            Col not in range(COLS) or 
            self.board[Row][Col][1] == color):
            # non legal move,
            # must be in range, and cannot be the same type of color as the original.
            print("move not legal")
            return
        # else, let's modify the board to put the pawn there
        temp = self.board[r][c]
        # empty board piece
        self.board[r][c] = (0,"",0)
        self.board[Row][Col] = temp

    def moveBishop(self):
        return
    
    def moveKnight(self):
        return
    
    def moveKing(self):
        return

    def moveQueen(self):
        return
    
    def moveRook(self):
        return
    def printBoard(self):
        for r in range(self.rows):
            print(self.board[r])
    
if __name__ == "__main__":
    Game = Chess()
    # specific pawn, move desired, color
    Game.printBoard()
    Game.movePawn(0,"forward","black")
    
    Game.printBoard()
    
    


