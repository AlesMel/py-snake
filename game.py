import pygame
import sys
from entity.food import Food
from entity.snake import Snake
from pygame.locals import *
from constants import Color, GameSettings
from point import Point, Directions

class Game():
    def __init__(self) -> None:
        print("Game created")
        self.screen = pygame.display.set_mode(GameSettings.RESOLUTION)
        self.last_direction: Point = Directions.RIGHT
        self.game_over = False
        
    def create_grid(self):
        grid_size = self.__get_grid_size()
        for row in range(grid_size[0]):
            for col in range(grid_size[1]):
                rect = pygame.Rect(row * GameSettings.DEFAULT_SQUARE_SIZE, col * GameSettings.DEFAULT_SQUARE_SIZE, GameSettings.DEFAULT_SQUARE_SIZE, GameSettings.DEFAULT_SQUARE_SIZE)
                if (row + col) % 2 == 0:
                    pygame.draw.rect(self.screen, Color.GRAY, rect)
                else:
                    pygame.draw.rect(self.screen, Color.BLACK, rect)
        pygame.display.flip()
        
    def start(self):
        print("Game started")
        pygame.init()
        clock = pygame.time.Clock()
        font = pygame.font.SysFont(None, 48)  # Font for "Game Over" text
        
        self.snake = Snake()
        self.food = Food()
        self.food.spawn(self.snake.snake_body)
        
        while True:
            # self.create_grid()
            self.screen.fill(Color.BLACK)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        self.can_move(Directions.UP)
                    if event.key == K_DOWN:
                        self.can_move(Directions.DOWN)
                    if event.key == K_LEFT:
                        self.can_move(Directions.LEFT)
                    if event.key == K_RIGHT:
                        self.can_move(Directions.RIGHT)
            self.snake.move(self.last_direction)
            self.snake.draw(self.screen)
            
            if self.snake.snake_body[0] == self.food.position:
                self.snake.snake_body.append(self.snake.snake_body[-1])
                self.food.spawn(self.snake.snake_body)
            self.food.draw(self.screen)
            
            if self.snake.check_out_of_bounds():
                self.game_over = True
                self.show_game_over_screen(font)
                break
            pygame.display.update()
            clock.tick(GameSettings.FPS)  # Set the desired frames per second (FPS)
        
    def __get_grid_size(self):
        squares = (self.screen.get_width() // GameSettings.DEFAULT_SQUARE_SIZE, self.screen.get_height() // GameSettings.DEFAULT_SQUARE_SIZE)
        return squares
    
    def show_game_over_screen(self, font):
        """Display the Game Over screen."""
        self.screen.fill((0, 0, 0))  # Clear screen with black background
        game_over_text = font.render("Game Over!", True, (255, 255, 255))  # White text
        text_rect = game_over_text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2 - 50))
        self.screen.blit(game_over_text, text_rect)
        
        restart_button_text = font.render("Restart", True, (255, 255, 255))
        restart_button_rect = restart_button_text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2 + 50))
        pygame.draw.rect(self.screen, (255, 0, 0), restart_button_rect.inflate(20, 10))  # Red button background
        self.screen.blit(restart_button_text, restart_button_rect)

        pygame.display.update()
        
        """Wait for the player to click the restart button or press a key."""
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if restart_button_rect.collidepoint(event.pos):
                        self.reset_game()
                
    def reset_game(self):
        """Reset the game state to start a new game."""
        self.game_over = False
        self.last_direction = Directions.RIGHT
        self.start()
        
    def can_move(self, direction):
        if len(self.snake.snake_body) < 2:
            self.last_direction = direction
        x = self.last_direction.value.x - direction.value.x
        y = self.last_direction.value.y - direction.value.y
        if abs(x) != 2 and abs(y) != 2:
            self.last_direction = direction
            
        
        
   

