# MainMenuScene.py
import pygwidgets
from pyghelpers import Scene
import constants


"""
This file defines the MainMenuScene class.
This scene is displayed at the beginning of the game, allowing the user to enter their name and start the game.
"""
# Define your Scene classes here, inheriting from Scene
class MainMenuScene(Scene):

    def __init__(self, window):
        self.window = window

        self.messageText = pygwidgets.DisplayText(window, (50, 50), 'Welcome to the Pong Game!', fontSize=36, justified='center')

        self.nameText = pygwidgets.DisplayText(window, (100, 130), ' Enter your name', fontSize=30, justified='center')

        self.inputTextScreen = pygwidgets.InputText(window, (100, 150), width=200, fontSize=36)

        self.startButton = pygwidgets.TextButton(window, (150, 200), 'Start Game')

        self.inputText = ''

    def getSceneKey(self):
        return constants.SCENE_A       

    def handleInputs(self, eventsList, keyPressedList):

        for event in eventsList:

            self.inputTextScreen.handleEvent(event)
            self.inputText = self.inputTextScreen.getValue()

            if self.startButton.handleEvent(event) and self.inputText != '':
                self.sendAll('userName', self.inputText) # Send the user's name to all the other scenes
                self.goToScene(constants.SCENE_B)
                self.inputTextScreen.clearText() # Clear the input text after the button is clicked

    def draw(self):
        self.window.fill((240, 128, 128))
        self.messageText.draw()
        self.startButton.draw()
        self.nameText.draw()
        self.inputTextScreen.draw()

