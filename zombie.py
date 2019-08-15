import pygame
from pygame.sprite import Sprite

class Zombie(Sprite):
    """Class to create a zombie that will spawn on screen."""
    
    def __init__(self, current_game):
        super().__init__()
        self.screen = current_game.screen
        self.image = pygame.image.load('images/zombie.png')
        self.image = pygame.transform.scale(self.image, (60, 78))
        self.image_rect = self.image.get_rect()
        self.image_rect.bottomleft = current_game.screen_rect.bottomleft