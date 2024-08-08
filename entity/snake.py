from point import Point
from typing import List
from constants import Color, GameSettings
import pygame

class Snake(pygame.sprite.Sprite):
    def __init__(self) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([GameSettings.DEFAULT_SQUARE_SIZE, GameSettings.DEFAULT_SQUARE_SIZE])
        self.image.fill(Color.GREEN)
        self.snake_body: List[Point] = [Point(1,0), Point(0, 0)]# [Point(GameSettings.DEFAULT_SQUARE_SIZE//2, GameSettings.DEFAULT_SQUARE_SIZE//2)] 
        self.rect = self.image.get_rect()
    
    def draw(self, screen):
        pygame.draw.rect(screen, Color.LIGHT_YELLOW, pygame.Rect(self.snake_body[0].x * GameSettings.DEFAULT_SQUARE_SIZE, self.snake_body[0].y * GameSettings.DEFAULT_SQUARE_SIZE, GameSettings.DEFAULT_SQUARE_SIZE, GameSettings.DEFAULT_SQUARE_SIZE))
        for segment in self.snake_body[1:]:
            pygame.draw.rect(screen, Color.WHITE, pygame.Rect(segment.x * GameSettings.DEFAULT_SQUARE_SIZE, segment.y * GameSettings.DEFAULT_SQUARE_SIZE, GameSettings.DEFAULT_SQUARE_SIZE, GameSettings.DEFAULT_SQUARE_SIZE), width=1)
        
    def move(self, direction):
        head = self.snake_body[0]
        head = Point(head.x + direction.value.x, head.y + direction.value.y)
        self.snake_body.pop()
        self.snake_body.insert(0, head)
    
    def check_out_of_bounds(self):
        if self.snake_body[0].x < 0 or self.snake_body[0].x * GameSettings.DEFAULT_SQUARE_SIZE >= GameSettings.RESOLUTION[0] or self.snake_body[0].y < 0 or self.snake_body[0].y * GameSettings.DEFAULT_SQUARE_SIZE >= GameSettings.RESOLUTION[1]:
            return True
        if self.snake_body[0] in self.snake_body[1:]:
            return True
    