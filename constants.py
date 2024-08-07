from pygame import color

class Color:
    WHITE = color.Color(255, 255, 255)
    BLACK = color.Color(0, 0, 0)
    GRAY = color.Color(128, 128, 128)
    
class GameSettings:
    RESOLUTION = (600, 600)
    DEFAULT_SQUARE_SIZE = 20