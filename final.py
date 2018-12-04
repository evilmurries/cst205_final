# Team 10 - Final Project
# M. Mariscal, C. Piwarski, W. Robleh


from javax.swing import JFrame, JButton
from java.awt import GridLayout

welcomeMessage ='Welcome to Animal Sounds Tic Tac Toe'
helpMessage = 'A two player game of tic tac toe where players win over squares by correctly guessing the animal sound sample.Each correct guess displays the animal represented by the sound.An incorrect guess results in the square being left open.The first player to complete a row of three for their shape wins!'
   
#Welcome message for our game
showInformation(welcomeMessage)
showInformation(helpMessage)




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
           
     