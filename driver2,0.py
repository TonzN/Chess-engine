import ui
import old_code.chessLibrary as cL
from math import floor

window_size = (600,600)

window = ui.NewWindow("Chess Game")
window.reSizeScreen(window_size)

screen = window.screen

grid = ui.grid(window_size, 75)
grid.generate(screen)

game = cL.Game(screen)
game.setup(grid.grid, 75)
game.loadPawns()
game.loadPieces()
print(game.Positions)

selectedTile = None
OriginalPos = None
selectedPiece = None
MoveToTile = None


while True: 
    window.NextFrame()
    pos = (floor(window.mousepos[0]/75)+1, floor(window.mousepos[1]/75)+1) #mouse cord to chess position
    pos = cL.files[pos[0]]+str(9-pos[1]) #turns the chess position into chess syntax

    if window.rightclick() == True: #when you click it does checks
        if pos in game.pieces and selectedPiece == None:
            selectedPiece = game.pieces[pos]
            OriginalPos = pos
            print(game.pieces[pos][1].name)
        else:
            selectedTile = pos
            if selectedPiece != None:
                MoveToTile = selectedPiece
            print(pos)
        
        if MoveToTile != None: #To move pieces after selected tile and piece
            print(selectedPiece, game.Positions[pos])

            selectedTile = None
            selectedPiece = None
            OriginalPos = None
            MoveToTile = None

    
    if window.leftclick() == True:
        selectedTile = None
        selectedPiece = None
        OriginalPos = None
        MoveToTile = None
