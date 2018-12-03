# Team 10 - Final Project

# One object of class player represents a player in the game of tic tac toe
class Player:

    # Constructor method for Class Player
    def __init__(self, inventory=[], squares=[], name='', shape=''):
        self.inventory = inventory
        self.name = name
        self.squares = squares
        slf.shape = shape

    # This method sets the name of the player
    def setName(self, name):
        self.name = name

    # This method returns the name of the player
    def getName(self):
        return self.name

    # This method adds a square to the player's won squares
    def addSquare(self, square):
        self.squares.append(square)

    # This method sets the shape for the player's squaresß
    def setShape(self, shape):
        self.shape = shape

    # This method returns the shape for the player's squares
    def getShape(self):
        return self.shape

