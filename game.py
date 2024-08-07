import pygame
import sys
from food import Food
from snake import Snake
from pygame.locals import *
from constants import Color, GameSettings

class Game():
    def __init__(self) -> None:
        print("Game created")
        self.screen = pygame.display.set_mode(GameSettings.RESOLUTION)
        print(GameSettings.RESOLUTION)
        
    def create_grid(self):
        print("Grid created")
        grid_size = self.__get_grid_size()
        for row in range(grid_size[0]):
            for col in range(grid_size[1]):
                rect = pygame.Rect(row * GameSettings.DEFAULT_SQUARE_SIZE, col * GameSettings.DEFAULT_SQUARE_SIZE, GameSettings.DEFAULT_SQUARE_SIZE, GameSettings.DEFAULT_SQUARE_SIZE)
                if (row + col) % 2 == 0:
                    pygame.draw.rect(self.screen, Color.GRAY, rect)
                else:
                    pygame.draw.rect(self.screen, Color.BLACK, rect)
        pygame.display.flip()
        pygame.init()
        
    def start(self):
        print("Game started")
        self.create_grid()
        snake = Snake()
        food = Food()
        while True:
           for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            pygame.display.update()
        
    def __get_grid_size(self):
        squares = (self.screen.get_width() // GameSettings.DEFAULT_SQUARE_SIZE, self.screen.get_height() // GameSettings.DEFAULT_SQUARE_SIZE)
        print(squares)
        return squares
        

