# Team 10 - Final Project
# M. Mariscal, C. Piwarski, W. Robleh


from javax.swing import JFrame, JButton
from java.awt import GridLayout

frame = JFrame("Animal Sounds Tic Tac Toe")
#frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
frame.setLocation(100,100)
frame.setSize(500,500)

frame.setLayout(GridLayout(3,3))

k = 0
for i in range(1,4):
   for j in range(1,4):
      k = k+1
      frame.add(JButton(str(k)))

frame.setVisible(True)
           
     