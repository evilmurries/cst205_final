# Team 10 - Final Project
# M. Mariscal, C. Piwarski, W. Robleh
# Developed with Python2 and JES


from java.awt import Dimension, GridLayout
from javax.swing import JButton, JFrame, JPanel, BoxLayout, Box
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
    self.sound = makeSound(sound)
    self.picture = makePicture(picture)
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


# One instance of class ticTacToeBoard creates the board for the game of 
# animal sounds tic tac toe.
class ticTacToeBoard(JFrame):

  # Constructor method for class ticTacToeBoard. Assembles the board
  def __init__(self):

    super(ticTacToeBoard, self).__init__(windowClosing=self.closeWindow)
    self.setTitle('Animal Sounds Tic Tac Toe')
    self.setSize(400,400)
    self.setLayout(GridLayout(3,3))

    self.createPlayers()
    self.makeAnimals()

    self.btn1 = JButton("Choose", actionPerformed = self.clickHere)
    self.add(self.btn1)

    self.btn2 = JButton("A", actionPerformed = self.clickHere)
    self.add(self.btn2)

    self.btn3 = JButton("Card", actionPerformed = self.clickHere)
    self.add(self.btn3)

    self.btn4 = JButton("Add", actionPerformed = self.clickHere)
    self.add(self.btn4)

    self.btn5 = JButton("Add", actionPerformed = self.clickHere)
    self.add(self.btn5)

    self.btn6 = JButton("Add", actionPerformed = self.clickHere)
    self.add(self.btn6)

    self.btn7 = JButton("Add", actionPerformed = self.clickHere)
    self.add(self.btn7)

    self.btn8 = JButton("Add", actionPerformed = self.clickHere)
    self.add(self.btn8)

    self.btn9 = JButton("Add", actionPerformed = self.clickHere)
    self.add(self.btn9)

    self.setVisible(True)

  # This method handles what happens when a button is pressed
  def clickHere(self, event):
    showInformation('clicked')

  # This method closes the window when clicked to
  def closeWindow(self, event):
    self.dispose()

  # This method creates the players for the game
  def createPlayers(self):
    self.player1 = Player(1)
    self.player2 = Player(2)
    self.player1.setName()
    self.player2.setName()
    self.player1.setShape('circle')
    self.player2.setShape('x')
    showInformation('Welcome %s and %s! Lets begin the game' % \
      (self.player1.getName(), self.player2.getName()))

  def makeAnimals(self):

    self.animals = []
    directory = os.path.dirname(__file__)

    # create animal objects
    soundPath = os.path.join(directory, 'animal sounds', 'bear_growl_y.wav')
    picPath = os.path.join(directory, 'animal pics', 'bear.jpg')
    bear = Animal('bear', soundPath, picPath)

    soundPath = os.path.join(directory, 'animal sounds', 'bird.wav')
    picPath = os.path.join(directory, 'animal pics', 'bird.jpg')
    bird = Animal('bird', soundPath, picPath)

    soundPath = os.path.join(directory, 'animal sounds', 'cat_y.wav')
    picPath = os.path.join(directory, 'animal pics', 'cat.jpg')
    cat = Animal('cat', soundPath, picPath)

    soundPath = os.path.join(directory, 'animal sounds', 'chicken.wav')
    picPath = os.path.join(directory, 'animal pics', 'chicken.jpg')
    chicken = Animal('chicken', soundPath, picPath)

    soundPath = os.path.join(directory, 'animal sounds', 'cow1.wav')
    picPath = os.path.join(directory, 'animal pics', 'cow.jpg')
    cow = Animal('cow', soundPath, picPath)

    soundPath = os.path.join(directory, 'animal sounds', 'crickets.wav')
    picPath = os.path.join(directory, 'animal pics', 'crickets.jpg')
    cricket = Animal('cricket', soundPath, picPath)

    soundPath = os.path.join(directory, 'animal sounds', 'dog_bark2.wav')
    picPath = os.path.join(directory, 'animal pics', 'dog.jpg')
    dog = Animal('dog', soundPath, picPath)

    soundPath = os.path.join(directory, 'animal sounds', 'dolphin.wav')
    picPath = os.path.join(directory, 'animal pics', 'dolphin.jpg')
    dolphin = Animal('dolphin', soundPath, picPath)

    soundPath = os.path.join(directory, 'animal sounds', 'donkey_x.wav')
    picPath = os.path.join(directory, 'animal pics', 'donkey.jpg')
    donkey = Animal('donkey', soundPath, picPath)

    soundPath = os.path.join(directory, 'animal sounds', 'horse.wav')
    picPath = os.path.join(directory, 'animal pics', 'horse.jpg')
    horse = Animal('horse', soundPath, picPath)

    soundPath = os.path.join(directory, 'animal sounds', 'monkey1.wav')
    picPath = os.path.join(directory, 'animal pics', 'monkey.jpg')
    monkey = Animal('monkey', soundPath, picPath)

    soundPath = os.path.join(directory, 'animal sounds', 'pig.wav')
    picPath = os.path.join(directory, 'animal pics', 'pig.jpg')
    pig = Animal('pig', soundPath, picPath)

    soundPath = os.path.join(directory, 'animal sounds', 'seal3.wav')
    picPath = os.path.join(directory, 'animal pics', 'seal.jpg')
    seal = Animal('seal', soundPath, picPath)

    soundPath = os.path.join(directory, 'animal sounds', 'whale.wav')
    picPath = os.path.join(directory, 'animal pics', 'whale.jpg')
    whale = Animal('whale', soundPath, picPath)

    # add animals to the list
    self.animals.append(bear)
    self.animals.append(bird)
    self.animals.append(cat)
    self.animals.append(chicken)
    self.animals.append(cow)
    self.animals.append(cricket)
    self.animals.append(dog)
    self.animals.append(dolphin)
    self.animals.append(donkey)
    self.animals.append(horse)
    self.animals.append(monkey)
    self.animals.append(pig)
    self.animals.append(seal)
    self.animals.append(whale)

  def printAnimals(self):
    for animal in self.animals:
      printNow(animal.getName())


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

# assemble tic tac toe board
board = ticTacToeBoard()

################################################################################
# animal image attributions
################################################################################

#HORSE
#By Nokota_Horses.jpg: Fran??ois Marchalderivative work: Dana boomer (talk) - 
#Nokota_Horses.jpg, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?
#curid=9456234

#BEAR
#By Yathin S Krishnappa - Own work, CC BY-SA 3.0, https://commons.wikimedia.org
#/w/index.php?curid=21436762

#BIRD
#By Dibyendu Ash - This is an image of Bar-throated Siva photographed at Fambong
# Lho WLS on March 2014.Previously published: Yes this file has been published 
#previously in my Facebook profile. Also the same is present in the Facebook 
#group called Indian Birds, CC BY-SA 3.0, https://commons.wikimedia.org/w/index
#.php?curid=31986161

#CAT
#By David Corby Edited by: Arad - Image:Kittyplya03042006.JPG, CC BY 2.5, 
#https://commons.wikimedia.org/w/index.php?curid=1839754

#CHICKEN
#By Andrei Niemim??ki from Turku, Finland - Friends, CC BY-SA 2.0,
# https://commons.wikimedia.org/w/index.php?curid=3769100

#COW
#https://commons.wikimedia.org/wiki/File:CH_cow_2_cropped.jpg#/media/
#File:CH_cow_2_cropped.jpg

#CRICKETS
#By Sean Wallace - Own work, CC BY-SA 3.0, 
#https://commons.wikimedia.org/w/index.php?curid=21277448

#DOG
#

#DOLPHIN
#By NASA - http://mediaarchive.ksc.nasa.gov/detail.cfm?mediaid=21807, 
#Public Domain, https://commons.wikimedia.org/w/index.php?curid=112006

#DONKEY
#Public Domain, https://commons.wikimedia.org/w/index.php?curid=123075

#MONKEY
#By Carlos Delgado - Own work, CC BY-SA 4.0, 
#https://commons.wikimedia.org/w/index.php?curid=34667538

#PIG
#By Johan Spaedtke - Own work, CC0, 
#https://commons.wikimedia.org/w/index.php?curid=26954959

#SEAL
#CC BY-SA 2.0 de, https://commons.wikimedia.org/w/index.php?curid=354703

#WHALE
#By Micha??l CATANZARITI - by Micha??l CATANZARITI, CC BY-SA 3.0, 
#https://commons.wikimedia.org/w/index.php?curid=396382
