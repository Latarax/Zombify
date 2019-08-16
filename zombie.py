import pygame
from pygame.sprite import Sprite
from settings import Settings
from random import randint

class Zombie(Sprite):
    """Class to create a zombie instance."""
    def __init__(self, current_game):
        """Initializes zombie's traits such as direction and position."""
        super().__init__()
        self.screen = current_game.screen
        self.settings = current_game.settings
        self.image = pygame.image.load('images/zombie.png')
        self.image = pygame.transform.scale(self.image, (60, 78))
        self.image_original = self.image
        self.image_flipped = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()

        # Generates either 0 or 1, with 0 spawning a zombie on the right 
        # and 1 spawning a zombie on the left
        self.left_right = randint(0, 1)
        
        if self.left_right == 0:
            self.rect.bottomright = current_game.screen_rect.bottomright
            self.rect.x += 50
            # Using float to hold x position in decimal
            self.x = float(self.rect.x)
        elif self.left_right == 1:
            self.rect.bottomleft = current_game.screen_rect.bottomleft
            self.image = self.image_flipped
            self.rect.x -= 50
            self.x = float(self.rect.x)

    def draw_zombie(self):
        """Displays zombie instance on screen."""
        self.screen.blit(self.image, self.rect)

    def update(self, current_game):
        """Updates zombie's position based on survivor position."""
        self.survivor_x = current_game.survivor.image_rect.x
        if self.survivor_x < self.x:
            self.image = self.image_original
            self.x -= self.settings.zombie_speed
            self.rect.x = self.x
            
        elif self.survivor_x > self.x:
            self.image = self.image_flipped
            self.x += self.settings.zombie_speed
            self.rect.x = self.x

        
