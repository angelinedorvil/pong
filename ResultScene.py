# GameScene.py
import pygame, sys
from pygame.locals import QUIT
import pygwidgets
from pyghelpers import Scene
from constants import SCENE_D, LIGHT_GRAY, TEAL


"""
This file defines the ResultScene class.
This scene is where the game result is displayed for the user.
The user can exit the game.
"""
class ResultScene(Scene):
  def __init__(self, window):
       self.window = window
       self.playerScore = None
       self.computerScore = None
       self.userName = None
       self.finalMess = pygwidgets.DisplayText(self.window, (150, 50), '') # Initialize the display for the final message
       self.finalImage = pygwidgets.DisplayText(self.window, (150, 50), '')
       self.exitButton = pygwidgets.TextButton(window, (350, 150), 'Exit', fontSize=36)

  def receive(self, receiveID, info): # Receive the player's score from the GameScene
      if receiveID == 'userName':
          self.userName = info
      if receiveID == 'playerScore':
          self.playerScore = info
      if receiveID == 'computerScore':
          self.computerScore = info

  def getSceneKey(self):
      return SCENE_D

  def handleInputs(self, eventsList, keyPressedList):
       for event in eventsList:
           if self.exitButton.handleEvent(event):
                pygame.quit()
                sys.exit() 

  def update(self):
      if self.computerScore > self.playerScore: # If the computer wins
          self.finalMess = pygwidgets.DisplayText(self.window, (10, 50), f'Better luck next time {self.userName}', fontSize=30, justified='center', textColor=TEAL)
          self.finalImage = pygwidgets.Image(self.window, (10, 70), 'images/lose.png')
      if self.computerScore < self.playerScore: # If the player wins
          self.finalMess = pygwidgets.DisplayText(self.window, (10, 50), f'{self.userName} won!', fontSize=50, justified='center', textColor=TEAL)
          self.finalImage = pygwidgets.Image(self.window, (10, 70), 'images/win.png')
      if self.computerScore == self.playerScore: # If it's a tie
          self.finalMess = pygwidgets.DisplayText(self.window, (250, 50), 'Tie Game', fontSize=50, justified='center', textColor=TEAL)
          self.finalImage = pygwidgets.Image(self.window, (10, 50), 'images/tie.png')

  def draw(self):
      self.window.fill(LIGHT_GRAY)
      self.exitButton.draw()
      self.displayScores = pygwidgets.DisplayText(self.window, (50, 0), f'{self.userName} Score: {self.playerScore}\nComputer Score: {self.computerScore}', fontSize=26)
      self.displayScores.draw()
      self.finalMess.draw()
      self.finalImage.draw()
