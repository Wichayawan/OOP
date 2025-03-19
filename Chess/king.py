from piece import Piece
class King(Piece): #inheritance
    def __init__(self, color):
        super().__init__(color)
        
    def move(self):
        print("King move")
        
class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        
    def move(self):
        print("Queen move")
        
king = King("white")
queen = Queen("black")
king.move()
queen.move()    