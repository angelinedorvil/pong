# PrepScene.py
import pygwidgets
from pyghelpers import Scene, CountDownTimer
from constants import SCENE_B, SCENE_C, LIGHT_GRAY, TEAL


"""
This file defines the PrepScene class.
This scene displays the instructions of the game, informing the user on the mechanics of the game.
"""
class PrepScene(Scene):

  def __init__(self, window):
      self.window = window

      self.userName = None 
      self.threeCount = pygwidgets.DisplayText(self.window, (300, 300), '', justified='center', fontSize=30) # Initialize the display for the countdown

      self.gameTimer = CountDownTimer(15) # Initialize the timer for the countdown
      self.gameTimer.start()

  def receive(self, receiveID, info):
    if receiveID == 'userName': # Receive the user's name from the main scene
        self.userName = info

  def getSceneKey(self):
      return SCENE_B

  def handleInputs(self, eventsList, keyPressedList):        
      pass

  def update(self):
      # Update the display time with the current timer value
      currentTime = self.gameTimer.getTimeInSeconds()

      self.instructions = pygwidgets.DisplayText(self.window, (150, 10),f"Hi {self.userName}!", fontSize=30, justified='center')

      self.takeSteps = pygwidgets.DisplayText(self.window, (10, 50),"Press the arrow up and down keys to move", fontSize=25, justified='center')

      self.takeSteps2 = pygwidgets.DisplayText(self.window, (10, 90),"Don't let the ball get past your post!!", fontSize=25, justified='center')

      self.takeSteps3 = pygwidgets.DisplayText(self.window, (10, 150),"You have 30 seconds, GO!!", fontSize=25, justified='center')

      self.myImage = pygwidgets.Image(self.window, (380, 50), 'images/arrow.png')

      # Timer and scene transition logic      
      if currentTime <= 3: # If the timer reaches 3 seconds, display the countdown
          self.threeCount = pygwidgets.DisplayText(self.window, (200, 200),f'{currentTime}', fontSize=90, justified='center', textColor=TEAL)
      if currentTime == 0:
          self.goToScene(SCENE_C)

  def draw(self):
      self.window.fill(LIGHT_GRAY)

      self.instructions.draw()
      self.takeSteps.draw()
      self.takeSteps2.draw()
      self.takeSteps3.draw()
      self.myImage.draw()
      self.threeCount.draw()
