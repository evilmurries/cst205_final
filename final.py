#!/usr/bin/env python3
# Team 10 - Final Project
# M. Mariscal, C. Piwarski, W. Robleh



board = [0,1,2,
         3,4,5, 
         6,7,8]

def show():
  print board[0],'|',board[1],'|',board[2]
  print '----------'
  print board[3],'|',board[4],'|',board[5]   
  print '----------'
  print board[6],'|',board[7],'|',board[8]                     
  
  welcomeMessage = 'Welcome to Animal Sounds Tic Tac Toe' 
  
  helpMessage = 'A two player game of tic tac toe where players win over squares by correctly guessing the animal sound sample.Each correct guess displays the animal represented by the sound.An incorrect guess results in the square being left open.The first player to complete a row of three for their shape wins!'
   
  #Welcome message for our game
  showInformation(welcomeMessage)
  showInformation(helpMessage)
  
              
  #name = requestString('Player 1 please type in your name:')
  #player1.setName(name)
  #name = requestString('Player 2 please type in your name :')
  #player2.setName(name)
  
  
           
     