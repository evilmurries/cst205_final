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


# One object of Animal square represents an animal complete with sounds.
class Animal:

  # Constructor method for class Animal
  def __init__(self, name='', sound=None, picture=None):  
    self.name = name
    self.sound = sound
    self.picture = picture

  # This method returns the name for the animal object
  def getName(self):
    return self.name

  # This method sets the name for the animal object
  def setName(self, name):
    self.name = name

  # This method returns the sound for the animal object
  def getSound(self):
    return self.sound

  # This method sets the sound for the animal object
  def setSound(self, sound):
    self.sound = sound

  # This method returns the picture for the animal object
  def getPicture(self):
    return self.picture

  # This method sets the picture for the animal object
  def setSound(self, picture):
    self.picture = picture


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

# here we can create the list of animals, example below
animalList = []
#cow = Animal('cow', 'moo.wav', 'cow.jpg')
#animalList.append(cow)

#tic tac toe board with individual buttons(I need to make them bigger though)

from java.awt import Dimension
from javax.swing import JButton, JFrame,JPanel,BoxLayout,Box

frame = JFrame()
frame.setTitle("Animal")
#frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
frame.setSize(500, 450)


panel = JPanel()
panel.setLayout(BoxLayout(panel, BoxLayout.Y_AXIS))
frame.add(panel)

###top panel
top = JPanel()
top.setLayout(BoxLayout(top, BoxLayout.X_AXIS))
b1 = JButton("?")
b2 = JButton("?")
b3 =JButton("?")
top.add(Box.createVerticalGlue())
top.add(b1)
top.add(Box.createRigidArea(Dimension(25, 0)))
top.add(b2)
top.add(Box.createRigidArea(Dimension(30, 0)))
top.add(b3)

###middle panel
middle = JPanel()
middle.setLayout(BoxLayout(middle, BoxLayout.X_AXIS))
b6 = JButton("?")
b7 = JButton("?")
b8 = JButton("?")
middle.add(b6)
middle.add(Box.createRigidArea(Dimension(25, 0)))
middle.add(b7)
middle.add(Box.createVerticalGlue())
middle.add(Box.createRigidArea(Dimension(30, 0)))
middle.add(b8)

###bottom panel
bottom = JPanel()
bottom.setLayout(BoxLayout(bottom, BoxLayout.X_AXIS))
b3 = JButton("?")
b4 = JButton("?")
b5 = JButton("?")
bottom.add(b3)
bottom.add(Box.createRigidArea(Dimension(25, 0)))
bottom.add(b4)
bottom.add(Box.createVerticalGlue())
bottom.add(Box.createRigidArea(Dimension(30, 0)))
bottom.add(b5)


panel.add(bottom)
panel.add(middle)
panel.add(top)
frame.setVisible(True)