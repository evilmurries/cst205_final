# Team 10 - Final Project
# M. Mariscal, C. Piwarski, W. Robleh


from javax.swing import JFrame, JButton
from java.awt import GridLayout

###############################################################################
# Classes
###############################################################################

# One object of class player represents a player in the game of tic tac toe
class Player:

    # Constructor method for Class Player
    def __init__(self, inventory=[], squares=[], name='', shape=''):
        self.inventory = inventory
        self.name = name
        self.squares = squares
        self.shape = shape

    # This method sets the name of the player
    def setName(self, name):
        self.name = name

    # This method returns the name of the player
    def getName(self):
        return self.name

    # This method adds a square to the player's won squares
    def addSquare(self, square):
        self.squares.append(square)

    # This method sets the shape for the player's squares
    def setShape(self, shape):
        self.shape = shape

    # This method returns the shape for the player's squares
    def getShape(self):
        return self.shape


###############################################################################
# Main Game Script
###############################################################################

welcomeMessage ='Welcome to Animal Sounds Tic Tac Toe'
helpMessage = 'A two player game of tic tac toe where players win over squares\
 by correctly guessing the animal sound sample. Each correct guess displays the\
 animal represented by the sound. An incorrect guess results in the square\
 being left open. The first player to complete a row of three for their shape\
  wins!'
   
#Welcome message for our game
showInformation(welcomeMessage)
showInformation(helpMessage)

# create players
player1 = Player()
player2 = Player()
name = requestString('Player 1: Type in your name.')
player1.setName(name)
name = requestString('Player 2: Type in your name.')
player2.setName(name)
showInformation('Welcome %s and %s! Lets begin the game' % (player1.getName(),\
 player2.getName()))

# Does this all belong in the main game loop? Like the text adventure?

frame = JFrame("Animal Sounds Tic Tac Toe")
#frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
frame.setLocation(100,100)
frame.setSize(500,500)

frame.setLayout(GridLayout(3,3))

k = 0
for i in range(1,4):
   for j in range(1,4):
      k = k+1
      frame.add(JButton(str("?")))

frame.setVisible(True)

           
     