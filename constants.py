from pygame import color
from point import Point
import enum

class Color:
    WHITE = color.Color(255, 255, 255)
    BLACK = color.Color(0, 0, 0)
    GRAY = color.Color(128, 128, 128)
    GREEN = color.Color(0, 255, 0)
    BLUE = color.Color(0, 0, 255)
    
class GameSettings:
    RESOLUTION = (600, 600)
    DEFAULT_SQUARE_SIZE = 20
    FPS = 5