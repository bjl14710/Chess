from tkinter import *

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

    def movePawn(self, select, direction, color) -> bool:
        # determine specific pawn.
        ROWS, COLS = len(self.board), len(self.board[0])
        red_directions = {"forward": (1,0), "back": (-1,0), "left":(0,1),"right":(0,-1)}
        black_directions = {"forward": (-1,0), "back": (1,0), "left":(0,-1),"right":(0,1)}
        r,c = self.findPiece("pawn",color,select)
        if r == -1 and c == -1:
            print("piece not found")
            return 
        if color == "black":
            # use black_directions
            dr,dc = black_directions[direction]
            Row = r + dr
            Col = c + dc
        elif color == "red":
            dr, dc = red_directions[direction]
            Row = r + dr
            Col = c + dc
            # use red directions
        else:
            print("not found")
            return False
        # make the move This should be it's own function since it will be used a lot.
        if (Row not in range(ROWS) or 
            Col not in range(COLS) or 
            self.board[Row][Col][1] == color):
            # non legal move,
            # must be in range, and cannot be the same type of color as the original.
            print("move not legal")
            return False
        # else, let's modify the board to put the pawn there
        # this swap should be too.
        self.swap(r,c,Row,Col)
        return [Row,Col]
        
    def moveBishop(self):
        return
    
    def moveKnight(self,direction,move,color):
        return
    
    def moveKing(self,direction):
        return

    def moveQueen(self,direction,move):
        return
    
    def moveRook(self,direction,move,color,select):
        # we return False if there is no way we can swap, else we return the final position
        notColor = color
        red_directions = {"forward": (1,0), "back": (-1,0), "left":(0,1),"right":(0,-1)}
        black_directions = {"forward": (-1,0), "back": (1,0), "left":(0,-1),"right":(0,1)}
        
        if color == "black":
            notColor = "red"
            dr, dc = black_directions[direction]
        elif color == "red":
            notColor = "black"
            dr, dc = red_directions[direction]
        row,col = self.findPiece("rook",color,select)
        
        def DFSMove(r,c,movesLeft):
            nonlocal dr, dc, notColor, row, col
            if (r not in range(self.rows) or c not in range(self.cols)
                or (self.board[r][c][1] == color and (r != row or c != col))):
                print("move not legal")
                # can't kill our own pieces or move outside of the board
                return False
            if movesLeft == 0:
                self.swap(row,col,r,c)
                return [r,c]
            if (self.board[r][c][1] == notColor):
                # we killed a piece
                self.swap(row,col,r,c)
                return [r,c]
            res = DFSMove(r+dr,c+dc,movesLeft-1)
            if res:
                return res
        # we reached the end
        return DFSMove(row,col,move)


    def swap(self,oR,oC,nR,nC):
        temp = self.board[oR][oC]
        self.board[oR][oC] = self.board[nR][nC]
        self.board[nR][nC] = temp

    def printBoard(self):
        for r in range(self.rows):
            print(self.board[r])
    
    def findPossibleSpots(self,piece,color,select):
        #def findPiece(self,piece,color,number):
        copy = self.board
        r,c = self.findPiece(piece,color,select)    
        spots = []
        visited = set()
        def backtracking(r,c,action):
            nonlocal spots
            if ((r,c) in visited):
                return 
            visited.add((r,c))
            if action == "rook":
                directions = ["forward","back","left","right"]
                for direction in directions:
                    for dist in range(1,8):
                        # check all 4 directions, recurse to check after that too. then 
                        pos = self.moveRook(direction,dist,color,select)
                        if not pos:
                            # we continue because we hit a wall and there is no way we can 
                            # keep going from there.
                            break
                        spots.append(pos)
                        backtracking(dist,c,action)
        if r != -1 or c != -1:
            backtracking(r,c,piece)
            self.board = copy
            if not spots:
                return []
            return self.removeDuplicates(spots)
            # we found the piece
    def removeDuplicates(self,arr):
        arr.sort()
        index = 1
        Size = len(arr)
        stack = [arr[0]]
        while index < Size:
            stack.append(arr[index])
            if stack[-2] == stack[-1]:
                stack.pop()
            index += 1
        return stack

if __name__ == "__main__":
    Game = Chess()
    # specific pawn, move desired, color
    Game.printBoard()
    # Game.movePawn(0,"forward","red")
    # Game.movePawn(0,"left","red")
    # Game.movePawn(1,"forward","black")
    # Game.movePawn(1,"forward","black")
    # Game.moveRook("forward",4,"red",0,True)
    # should return Null
    # good, can't do any moves no spots
    print(Game.findPossibleSpots("rook","black",1))
    # move pawn out of the way
    Game.movePawn(7,"forward","black")
    Game.movePawn(7,"left","black")
    Game.moveRook("forward",4,"black",1)
    Game.moveRook("left",4,"black",1)
    print(Game.findPiece("rook","black",1))
    #def findPiece(self,piece,color,number):
    
    print()
    print()
    print()
    print(Game.findPossibleSpots("rook","black",1))
    print()
    print()
    print()
    # movePawn(self, select, move, color)
    # moveRook(self,direction,move,color,select)
    # def findPossibleSpots(self,piece,color,select):s
    Game.printBoard()
    
    
    


