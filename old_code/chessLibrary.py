import ui
import engine

white = "White"
black = "Black"

piecesimg = {
    "Pawn":     ["chesspieces\WhitePawn.png", "chesspieces\BlackPawn.png"],
    "Knight":   ["chesspieces\WhiteKnight.png", "chesspieces\BlackKnight.png"],
    "Bishop":   ["chesspieces\WhiteBishop.png", "chesspieces\BlackBishop.png"],
    "Rook":     ["chesspieces\WhiteRook.png", "chesspieces\BlackRook.png"],
    "Queen":    ["chesspieces\WhiteQueen.png", "chesspieces\BlackQueen.png"],
    "King":     ["chesspieces\WhiteKing.png", "chesspieces\BlackKing.png"],
}

files = {
    1: "a",
    2: "b",
    3: "c",
    4: "d",
    5: "e",
    6: "f",
    7: "g",
    8: "h",
}

def player(board):
    pass

class Pawn():
    def __init__(self, startpos, team, gamePos, screen):
        self.pos = startpos
        self.StartingPos = True
        self.name = team+"pawn"
        if team == "white":
            self.img = ui.image(screen, piecesimg["Pawn"][0], gamePos)
            self.val = 1
        elif team == "black": #gives appropriate value 
            self.val = -1
            self.img = ui.image(screen, piecesimg["Pawn"][1], gamePos)
        #print(self.team, self.val)
    
    def moveTo(self, file, pieces):
        file = file[0]
        rank = int[file[1]]
        moves = [file+str(rank+1)] #possible moves for pawn
        if self.StartingPos:
            moves.append(file+str(rank+2)) #lets pawn move 2 at start
        #print(moves)

        return moves

class Knight():
    def __init__(self):
        self.Value = 3
    
    def isLegal(self):
        pass

class Bishop():
    def __init__(self):
        self.Value = 3

class Rook():
    def __init__(self):
        self.Value = 5
    def isLegal(self):
        pass

class Queen():
    def __init__(self):
        self.Value = 9
    def isLegal(self):
        pass

class King():
    def __init__(self):
        self.Value = 1000
    def isLegal(self):
        pass

class Game:
    def __init__(self, screen):
        self.debugMode = False

        #meta gamedata
        self.screen = screen

        self.Positions = {

        }

        self.pieces = {

        }
    
    def setup(self, grid, cellsize):
        gridl = len(grid)
        for i in range(gridl):
            for z in range(gridl):
                self.Positions[files[z+1]+str(i+1)] = (z*cellsize, (gridl-1-i)*cellsize) # Access positions with chess syntax
        if self.debugMode == True:
            print("Successfully loaded gameboard")

    def move(self, piece, newPos):
        piece.moveTo(newPos, self.pieces)

    def loadPawns(self):
        #WhitePawns
        for i in range(1,9):
            pos = files[i]+"2"
            self.pieces[pos] = Pawn(pos, "white", self.Positions[pos], self.screen)

        #BlackPawns
        for i in range(1,9):
            pos = files[i]+"7"
            self.pieces[pos] = Pawn(pos, "black", self.Positions[pos], self.screen)

    def loadPieces(self):
        #white
        
        self.pieces[files[2]+"1"]  = (ui.image(self.screen, piecesimg["Knight"][0], self.Positions[files[2]+"1"]), "WhiteKnight")
        self.pieces[files[7]+"1"]  = (ui.image(self.screen, piecesimg["Knight"][0], self.Positions[files[7]+"1"]), "WhiteKnight")
        self.pieces[files[3]+"1"]  = (ui.image(self.screen, piecesimg["Bishop"][0], self.Positions[files[3]+"1"]), "WhiteBishop")
        self.pieces[files[6]+"1"]  = (ui.image(self.screen, piecesimg["Bishop"][0], self.Positions[files[6]+"1"]), "WhiteBishop")
        self.pieces[files[1]+"1"]  = (ui.image(self.screen, piecesimg["Rook"][0], self.Positions[files[1]+"1"]),   "WhiteRook")
        self.pieces[files[8]+"1"]  = (ui.image(self.screen, piecesimg["Rook"][0], self.Positions[files[8]+"1"]),   "WhiteRook")
        self.pieces[files[4]+"1"]  = (ui.image(self.screen, piecesimg["Queen"][0], self.Positions[files[4]+"1"]),  "WhiteQueen")
        self.pieces[files[5]+"1"]  = (ui.image(self.screen, piecesimg["King"][0], self.Positions[files[5]+"1"]),   "WhiteKing")
        if self.debugMode == True:
            print("Successfully loaded white pieces")

        
        self.pieces[files[2]+ "8"]  = (ui.image(self.screen, piecesimg["Knight"][1], self.Positions[files[2]+"8"]),"BlackKnight")
        self.pieces[files[7]+ "8"]  = (ui.image(self.screen, piecesimg["Knight"][1], self.Positions[files[7]+"8"]),"BlackKnight")
        self.pieces[files[3]+ "8"]  = (ui.image(self.screen, piecesimg["Bishop"][1], self.Positions[files[3]+"8"]),"BlackBishop")
        self.pieces[files[6]+ "8"]  = (ui.image(self.screen, piecesimg["Bishop"][1], self.Positions[files[6]+"8"]),"BlackBishop")
        self.pieces[files[1]+ "8"]  = (ui.image(self.screen, piecesimg["Rook"][1], self.Positions[files[1]+"8"])  ,"BlackRook") 
        self.pieces[files[8]+ "8"]  = (ui.image(self.screen, piecesimg["Rook"][1], self.Positions[files[8]+"8"])  ,"BlackRook")
        self.pieces[files[4]+ "8"]  = (ui.image(self.screen, piecesimg["Queen"][1], self.Positions[files[4]+"8"]) ,"BlackQueen")
        self.pieces[files[5]+ "8"]  = (ui.image(self.screen, piecesimg["King"][1], self.Positions[files[5]+"8"])  ,"BlackKing") 
        if self.debugMode == True:
            print("Successfully loaded Black pieces")
        
    def loadGame(self):
        self.loadPawns()
        if self.debugMode == True:
            print("Successfully loaded pawns")
        self.loadPieces()
        if self.debugMode == True:
            print("Successfully loaded pieces")
    