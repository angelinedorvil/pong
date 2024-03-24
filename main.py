import pygame, sys
from pygame.locals import QUIT
from pyghelpers import SceneMgr
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, FRAMES_PER_SECOND
from MainMenuScene import MainMenuScene
from PrepScene import PrepScene
from GameScene import GameScene
from ResultScene import ResultScene


def main():
    pygame.init()
    windowSize = (WINDOW_WIDTH, WINDOW_HEIGHT)
    screen = pygame.display.set_mode(windowSize)


    # Create 
    scenesList = [MainMenuScene(screen),
                  PrepScene(screen),
                  GameScene(screen),
                  ResultScene(screen)]

    # Create the Scene Manager
    oSceneMgr = SceneMgr(scenesList, FRAMES_PER_SECOND)

    # Main game loop
    while True:
        # Scene management, event handling, updates, and rendering
        oSceneMgr.run()

        pygame.display.update()

if __name__ == "__main__":
    main()
