# Team 10 - Final Project
# M. Mariscal, C. Piwarski, W. Robleh


from javax.swing import JFrame, JButton
from java.awt import GridLayout
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
  chicken = Animal('chicken', soundsPath + 'chicken.wav', picsPath + 'chicken.jpg')
  cow = Animal('cow', soundsPath + 'cow1.wav', picsPath + 'cow.jpg')
  cricket = Animal('cricket', soundsPath + 'crickets.wav', picsPath + 'crickets.jpg')
  dog = Animal('dog', soundsPath + 'dog_bark2.wav', picsPath + 'dog.jpg')
  dolphin = Animal('dolphin', soundsPath + 'dolphin.wav', picsPath + 'dolphin.jpg')
  donkey = Animal('donkey', soundsPath + 'donkey_x.wav', picsPath + 'donkey.jpg')
  horse = Animal('horse', soundsPath + 'horse.wav', picsPath + 'horse.jpg')
  monkey = Animal('monkey', soundsPath + 'monkey1.wav', picsPath + 'monkey.jpg')
  pig = Animal('pig', soundsPath + 'pig.wav', picsPath + 'pig.jpg')
  seal = Animal('seal', soundsPath + 'seal3.wav', picsPath + 'seal.jpg')
  whale = Animal('whale', soundsPath + 'whale.wav', picsPath + 'whale.jpg')

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
frame = JFrame("Sounds")
#frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
frame.setLocation(100,100)
frame.setSize(600,600)
frame.setLayout(GridLayout(3,3))
b1=JButton
b2=JButton
b3=JButton
b4=JButton
b5=JButton
b6=JButton
b7=JButton
b8=JButton
b9=JButton

k = 0
for i in range(1,10):
   for j in range(1,2):
      k = k+1
      frame.add(JButton(str(k)))
frame.setVisible(True)


################################################################################
# animal image attributions
################################################################################

#HORSE
#By Nokota_Horses.jpg: François Marchalderivative work: Dana boomer (talk) - 
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
#By Andrei Niemimäki from Turku, Finland - Friends, CC BY-SA 2.0,
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
#By Michaël CATANZARITI - by Michaël CATANZARITI, CC BY-SA 3.0, 
#https://commons.wikimedia.org/w/index.php?curid=396382

