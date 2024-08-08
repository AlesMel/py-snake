from point import Point
from constants import Color, GameSettings
from random import randint
import pygame

class Food():
    def __init__(self):
        self.position: Point = Point(-1, -1)
    
    def spawn(self, snake_body):
        while True:
            x = randint(0, GameSettings.RESOLUTION[0] // GameSettings.DEFAULT_SQUARE_SIZE - 1)
            y = randint(0, GameSettings.RESOLUTION[1] // GameSettings.DEFAULT_SQUARE_SIZE - 1)
            position = Point(x, y)
            if position not in snake_body:
                self.position = position
                break
            
    def draw(self, screen):
        pygame.draw.rect(screen, Color.BLUE, pygame.Rect(self.position.x * GameSettings.DEFAULT_SQUARE_SIZE, self.position.y * GameSettings.DEFAULT_SQUARE_SIZE, GameSettings.DEFAULT_SQUARE_SIZE, GameSettings.DEFAULT_SQUARE_SIZE))
        
    