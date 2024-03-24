# GameScene.py
import pygame, sys
from pygame.locals import QUIT
import random
import pygwidgets
from pyghelpers import Scene, CountDownTimer
from constants import SCENE_C, SCENE_D, WINDOW_HEIGHT, Y_CCOORD, Y_CICOORD, Y_UCOORD, Y_SPEED, BALL_SPEED, X_CICOORD, X_UCOORD, X_CCOORD, WINDOW_WIDTH, WHITE, BLACK, PURPLE, YELLOW, TEAL


"""
This file defines the GameScene class.
This scene is where the game variables, structures and mechanics are handle. 
Basically, this scene is the main game scene.
"""
class GameScene(Scene):
  # Implement game logic, handling events, updates, and rendering
  def __init__(self, window):
      self.window = window

      self.myImage = pygwidgets.Image(self.window, (10, 20), 'images/field.png') # Background image for game

      self.playerScore = 0

      self.computerScore = 0

      self.userName = None 

      self.displayTime = pygwidgets.DisplayText(self.window, (400, 0), '', justified='center', fontSize=30) # Initialize the display for the countdown

      self.youComputerField = pygwidgets.DisplayText(self.window, (150, 0), '', justified='center', fontSize=30) # Initialize the display for game scores


      self.userPaddle = pygame.Rect(X_UCOORD, Y_UCOORD, 20, 50)  # Player paddle
      self.computerPaddle = pygame.Rect(X_CCOORD, Y_CCOORD, 20, 50)  
      self.ball = pygame.Rect(X_CICOORD, Y_CICOORD, 20, 20)  # Ball as a square for simplicity

      self.ballVelocity = pygame.Vector2(random.choice([-1, 1]), random.choice([-1, 1])) * BALL_SPEED # Ball velocity calcuation

      self.gameTimer = CountDownTimer(45)
      self.gameTimer.start()

  def receive(self, receiveID, info):
    if receiveID == 'userName': # Receive the user's name from the main scene
        self.userName = info

  def getSceneKey(self):
      return SCENE_C

  def handleInputs(self, eventsList, keyPressedList):        
      for event in eventsList: # Handle events for the game only for arrow keys 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                self.userPaddle.y -= 20
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.userPaddle.y += 20

  def update(self):
      # Update the display time with the current timer value
      currentTime = self.gameTimer.getTimeInSeconds()

      self.displayTime = pygwidgets.DisplayText(self.window, (400, 0), f'{currentTime}', fontSize=30)

      self.youComputerField = pygwidgets.DisplayText(self.window, (150, 0),f'{self.userName}:{self.playerScore}     Computer:{self.computerScore}', justified='center', fontSize=30) # Update the display for game scores

      # Update the ball position based on the ball velocity
      self.ball.x += self.ballVelocity.x 
      self.ball.y += self.ballVelocity.y

      # Ball collision with walls
      if self.ball.top <= 0 or self.ball.bottom >= WINDOW_HEIGHT:
          self.ballVelocity.y *= -1
      if self.ball.x <= 0 or self.ball.x >= WINDOW_WIDTH:
          # Update scores and reset ball
          if self.ball.x <= 0:
              self.computerScore += 1
          else:
              self.playerScore += 1
          # Reset ball position to the center and randomly set direction
          self.ball.x = X_CICOORD
          self.ball.y = Y_CICOORD
          self.ballVelocity = pygame.Vector2(random.choice([-1, 1]), random.choice([-1, 1])) * BALL_SPEED

      # Collision with paddles
      if self.ball.colliderect(self.userPaddle) or self.ball.colliderect(self.computerPaddle):
          self.ballVelocity.x *= -1

      move_chance = 0.8  # 80% chance to move correctly towards the ball
      if random.random() < move_chance:
          # Move computer paddle towards the ball
          if self.ball.y < self.computerPaddle.y + self.computerPaddle.height / 2:
              self.computerPaddle.y -= Y_SPEED
          elif self.ball.y > self.computerPaddle.y + self.computerPaddle.height / 2:
              self.computerPaddle.y += Y_SPEED

      # Ensure paddles stay within the window boundaries
      self.computerPaddle.y = max(0, min(WINDOW_HEIGHT - self.computerPaddle.height, self.computerPaddle.y))
      self.userPaddle.y = max(0, min(WINDOW_HEIGHT - self.userPaddle.height, self.userPaddle.y))

      # Timer and scene transition logic      
      if currentTime <= 5:
        self.displayTime = pygwidgets.DisplayText(self.window, (180, 20),f'{currentTime}', fontSize=200, justified='center', textColor=TEAL)
      if currentTime == 0:
        self.send('scene D', 'playerScore', self.playerScore) # Send the player's score to the ResultScene
        self.send('scene D', 'computerScore', self.computerScore)
        self.goToScene(SCENE_D)

  def draw(self):
      self.window.fill(WHITE)

      self.myImage.draw()

      self.youComputerField.draw()

      self.displayTime.draw()

      pygame.draw.rect(self.window, BLACK, self.userPaddle)
      pygame.draw.rect(self.window, PURPLE, self.computerPaddle)
      pygame.draw.ellipse(self.window, YELLOW, self.ball)
      pygame.display.update()
