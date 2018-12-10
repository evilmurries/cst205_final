# Team 10 - Final Project
# M. Mariscal, C. Piwarski, W. Robleh
# Developed with Python2 and JES


from java.awt import Dimension, GridLayout
from javax.swing import JButton, JFrame, JPanel, BoxLayout, Box
import os
import random


###############################################################################
# Classes
###############################################################################

# One object of class player represents a player in the game of tic tac toe
class Player:

    # Constructor method for Class Player
    def __init__(self, number, animals=[], name='', shape=''):
        self.number = number
        self.name = name
        self.animals = animals
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
    def addAnimal(self, animal):
        self.animals.append(animal)
        
    def getAnimals(self):
      return self.animals

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
    self.isUsed = False

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

  # Returns the won status of the animal object
  def animalUsed(self):
    self.isUsed = True
  
  # Returns False if the animal object has not been used in the game yet.
  def isWon(self):
    return self.isUsed

  # This method describes the print characteristics of class Player
  def __str__(self):
    return self.name


# One instance of class ticTacToeBoard creates the board for the game of 
# animal sounds tic tac toe.
class ticTacToeBoard(JFrame):

  # Constructor method for class ticTacToeBoard. Assembles the board
  def __init__(self):

    super(ticTacToeBoard, self).__init__(windowClosing=self.closeWindow)
    self.setTitle('Animal Sounds Tic Tac Toe')
    self.setSize(400,400)
    self.setLayout(GridLayout(3,3))

    # create variables
    self.createPlayers()
    self.makeAnimals()
    self.answerKey = ['1', '2', '3',
                  '4', '5', '6',
                  '7', '8', '9']
    self.playerTurn = self.player1
    self.isGameWon = False
    self.winner = ''

    # Create and add buttons
    self.btn1 = JButton("1", actionPerformed = self.clickHere)
    self.add(self.btn1)

    self.btn2 = JButton("2", actionPerformed = self.clickHere)
    self.add(self.btn2)

    self.btn3 = JButton("3", actionPerformed = self.clickHere)
    self.add(self.btn3)

    self.btn4 = JButton("4", actionPerformed = self.clickHere)
    self.add(self.btn4)

    self.btn5 = JButton("5", actionPerformed = self.clickHere)
    self.add(self.btn5)

    self.btn6 = JButton("6", actionPerformed = self.clickHere)
    self.add(self.btn6)

    self.btn7 = JButton("7", actionPerformed = self.clickHere)
    self.add(self.btn7)

    self.btn8 = JButton("8", actionPerformed = self.clickHere)
    self.add(self.btn8)

    self.btn9 = JButton("9", actionPerformed = self.clickHere)
    self.add(self.btn9)

    self.setVisible(True)

    showInformation('%s: It is your turn' % self.playerTurn.getName())

  # This method handles what happens when a button is pressed
  # Used this source to determine the name of the event
  # https://stackoverflow.com/questions/8084679/jython-swing-passing-more-
  # than-self-and-event-on-a-button-press
  def clickHere(self, event):
    self.sender = event.getSource()
		
    #Test to play sound
    # select random animal
    loopFlag = True
    self.randomAnimal = 0
    while loopFlag == True:
      self.randomAnimal = random.randint(0, 13)
      if self.animals[self.randomAnimal].isWon() == False:
        loopFlag = False
    
    # play sound
    showInformation('Press Enter When You Are Ready To Hear Animal Sound')
    play(self.animals[self.randomAnimal].getSound())
    
    
    # handle user guess
    response = requestString('What animal do you think makes this sound?')
    response = response.lower()
    showInformation('Your guess: %s' % response)
    
    # check user input for correctness
    # if they win the square
    if response == self.animals[self.randomAnimal].getName():
      self.animals[self.randomAnimal].animalUsed()
      self.playerTurn.addAnimal(self.animals[self.randomAnimal])
      showInformation('Correct!')
      self.square = int(self.sender.getText())
      self.square -= 1
      self.sender.setText(self.playerTurn.getShape())
      self.answerKey[self.square] = self.playerTurn.getShape()
      if self.isGameOver():
        self.endGame(self.playerTurn)
    # if they lose the square
    else:
      showInformation('Sorry, incorrect guess. Next players turn.')

    # set up next round
    self.playerTurn = self.changePlayerTurn(self.playerTurn)
    showInformation('%s: It is your turn' % self.playerTurn.getName())
    return

  # check to see if anyone won the game

  def isGameOver(self):
    
    if self.answerKey[0] == self.answerKey[1] and self.answerKey[1] == self.answerKey[2]:
      return True
    elif self.answerKey[3] == self.answerKey[4] and self.answerKey[4] == self.answerKey[5]:
      return True
    elif self.answerKey[6] == self.answerKey[7] and self.answerKey[7] == self.answerKey[8]:
      return True
    elif self.answerKey[0] == self.answerKey[3] and self.answerKey[3] == self.answerKey[6]:
      return True
    elif self.answerKey[1] == self.answerKey[4] and self.answerKey[4] == self.answerKey[7]:
      return True
    elif self.answerKey[2] == self.answerKey[5] and self.answerKey[5] == self.answerKey[8]:
      return True
    elif self.answerKey[0] == self.answerKey[4] and self.answerKey[4] == self.answerKey[8]:
      return True
    elif self.answerKey[2] == self.answerKey[4] and self.answerKey[4] == self.answerKey[6]:
      return True
    else:
      return False
  
#Artify to change final pic for winning player
  def Artify(self, pic):
    for p in getPixels(pic):
      b = getBlue(p)
      g = getGreen(p)
      r = getRed(p)
      # apply Artify
      r = calculateColor(r)
      b = calculateColor(b)
      g = calculateColor(g)
      color = makeColor(r, g, b)
      setColor(p, color) 
    return pic
  

  # end the game 
  def endGame(self, winningPlayer):
    self.winningAnimals = winningPlayer.getAnimals()
    showInformation('Congratulations on winning %s! Enjoy your animal parade' % winningPlayer.getName())
		
    #animal parade
    #make empty canvas for winning 3 pics to be shown
    self.canvas = makeEmptyPicture(1100, 800)
    #self.canvas = self.winningAnimals[0].
    #self.pic = []
    #self.pic[0] = self.winningAnimals[0]
    #self.pic[1] = self.winningAnimals[1]
    #self.pic[2] = self.winningAnimals[2]
    
    #Place pics in blank canvas
    self.canvas = copyInto(self.winningAnimals[0].getPicture(), self.canvas, 10, 10)
    self.canvas = copyInto(self.winningAnimals[1].getPicture(), self.canvas, 350, 10)
    self.canvas = copyInto(self.winningAnimals[2].getPicture(), self.canvas, 700, 10)
    
    #Artify canvas
   # self.canvas = self.Artify(self.canvas)
    #show canvas
    show(self.canvas)
    # close window
    showInformation('Thank you for playing!')
    self.closeWindow(self)
  
  # This method closes the window when clicked to
  def closeWindow(self, event):
    self.dispose()

  # This method creates the players for the game
  def createPlayers(self):
    self.player1 = Player(1)
    self.player2 = Player(2)
    self.player1.setName()
    self.player2.setName()
    self.player1.setShape('O')
    self.player2.setShape('X')
    showInformation('Welcome %s and %s! Lets begin the game' % \
      (self.player1.getName(), self.player2.getName()))

  # This method creates a list of animals for the game
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

  # This method prints out the names of all the animals in the game
  def printAnimals(self):
    for animal in self.animals:
      printNow(animal.getName())

  # This method changes which player's turn it is
  def changePlayerTurn(self, currentPlayer):
    if currentPlayer.getNumber() == 1:
      return self.player2
    else:
      return self.player1


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