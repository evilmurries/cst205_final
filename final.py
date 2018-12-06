# Team 10 - Final Project
# M. Mariscal, C. Piwarski, W. Robleh


from javax.swing import JFrame, JButton
from java.awt import GridLayout
from java.awt import Dimension
from javax.swing import JButton, JFrame,JPanel,BoxLayout,Box
import os

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

  def __str__(self):
    print self.name

################################################################################
# functions
################################################################################

def makeAnimals():

  animals = []
  # create animal objects
  bear = Animal('bear')
  bird = Animal('bird')
  cat = Animal('cat')
  chicken = Animal('chicken')
  cow = Animal('cow')
  cricket = Animal('cricket')
  dog = Animal('dog')
  dolphin = Animal('dolphin')
  donkey = Animal('donkey')
  horse = Animal('horse')
  monkey = Animal('monkey')
  pig = Animal('pig')
  seal = Animal('seal')
  whale = Animal('whale')

  # add animals to the list
  animals.append(bear)
  animals.append(bird)
  animals.append(cat)
  animals.append(chicken)
  animals.append(cow)
  animals.append(cricket)
  animals.append(dog)
  animals.append(dolphin)
  animals.append(donkey)
  animals.append(horse)
  animals.append(monkey)
  animals.append(pig)
  animals.append(seal)
  animals.append(whale)
  return animals



################################################################################
# Main Game Script
################################################################################

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
animalList = makeAnimals()
for animal in animalList:
  printNow(animal.getName())

#tic tac toe board with individual buttons(I need to make them bigger though)

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
b4 = JButton("?")
b5 = JButton("?")
b6 = JButton("?")
middle.add(b4)
middle.add(Box.createRigidArea(Dimension(25, 0)))
middle.add(b5)
middle.add(Box.createVerticalGlue())
middle.add(Box.createRigidArea(Dimension(30, 0)))
middle.add(b6)

###bottom panel
bottom = JPanel()
bottom.setLayout(BoxLayout(bottom, BoxLayout.X_AXIS))
b7 = JButton("?")
b8 = JButton("?")
b9 = JButton("?")
bottom.add(b7)
bottom.add(Box.createRigidArea(Dimension(25, 0)))
bottom.add(b8)
bottom.add(Box.createVerticalGlue())
bottom.add(Box.createRigidArea(Dimension(30, 0)))
bottom.add(b9)


panel.add(bottom)
panel.add(middle)
panel.add(top)
frame.setVisible(True)