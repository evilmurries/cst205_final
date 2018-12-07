# Team 10 - Final Project
# M. Mariscal, C. Piwarski, W. Robleh


from java.awt import Dimension
from javax.swing import JButton, JFrame,JPanel,BoxLayout,Box
import os


###############################################################################
# Classes
###############################################################################

# One object of class player represents a player in the game of tic tac toe
class Player:

    # Constructor method for Class Player
    def __init__(self, number, inventory=[], squares=[], name='', shape=''):
        self.number = number
        self.inventory = inventory
        self.name = name
        self.squares = squares
        self.shape = shape

    # This method sets the name of the player
    def setName(self):
      name = ''
      while name == '':
        name = requestString('Player %d: Type in your name.' % self.number)
      self.name = name

    # This method returns the name of the player
    def getName(self):
        return self.name

    # This method sets the player number
    def setNumber(self, number):
      self.number = number

    # This method returns the player number
    def getNumber(self):
      return self.number

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
    self.wasUsed = False

  # This method returns the name for the animal object
  def getName(self):
    return self.name

  # This method sets the name for the animal object
  def setName(self):
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

  # Returns False if the animal object has not been used in the game yet.
  def wasUsed(self):
    return self.wasUsed

  # This method describes the print characteristics of class Player
  def __str__(self):
    print self.name

################################################################################
# functions
################################################################################

def makeAnimals():
  soundsPath = setMediaFolder()
  picsPath = setMediaFolder()
  animals = []
  # create animal objects
  bear = Animal('bear', soundsPath + 'bear_growl_y.wav', picsPath + 'bear.jpg')
  bird = Animal('bird', soundsPath + 'bird.wav', picsPath + 'bird.jpg')
  cat = Animal('cat' , soundsPath + 'cat_y.wav', picsPath + 'cat.jpg')
  chicken = Animal('chicken', soundsPath + 'chicken.wav', picsPath + 'bear.jpg')
  cow = Animal('cow', soundsPath + 'cow1.wav', picsPath + 'bear.jpg')
  cricket = Animal('cricket', soundsPath + 'crickets.wav', picsPath + 'bear.jpg')
  dog = Animal('dog', soundsPath + 'dog_bark2.wav', picsPath + 'dog.jpg')
  dolphin = Animal('dolphin', soundsPath + 'dolphin.wav', picsPath + 'bear.jpg')
  donkey = Animal('donkey', soundsPath + 'donkey_x.wav', picsPath + 'bear.jpg')
  horse = Animal('horse', soundsPath + 'horse.wav', picsPath + 'bear.jpg')
  monkey = Animal('monkey', soundsPath + 'monkey1.wav', picsPath + 'bear.jpg')
  pig = Animal('pig', soundsPath + 'pig.wav', picsPath + 'bear.jpg')
  seal = Animal('seal', soundsPath + 'seal3.wav', picsPath + 'bear.jpg')
  whale = Animal('whale', soundsPath + 'whale.wav', picsPath + 'bear.jpg')

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

# Main game loop after 
def game():
  return

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
player1 = Player(1)
player2 = Player(2)
player1.setName()
player2.setName()
player1.setShape('circle')
player2.setShape('x')
showInformation('Welcome %s and %s! Lets begin the game' % (player1.getName(),\
 player2.getName()))

# create animal objects
animalList = makeAnimals()

#tic tac toe board with individual buttons

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