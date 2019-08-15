import pygame
import math
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Controls bullet attributes such as size and physics."""
    def __init__(self, current_game):
        super().__init__()
        self.settings = current_game.settings
        self.screen = current_game.screen
        self.survivor = current_game.survivor
        self.image = pygame.image.load('images/tempgun.bmp')
        self.image_rect = self.image.get_rect()
        self.image_rect.midtop = current_game.survivor.image_rect.midtop
        self.image_copy = pygame.transform.rotate(self.image, int(self.survivor.angle + 180))
        self.mouse_pos_x, self.mouse_pos_y = pygame.mouse.get_pos()
        self.vec_x = self.mouse_pos_x - self.image_rect.x
        self.vec_y = self.mouse_pos_y - self.image_rect.y

    def draw_bullet(self):
        """Draw updated bullet onto screen."""
        #self._update_bullet_test()
        #pygame.draw.rect(self.screen, (0, 0, 0), self.image_rect)
        self.screen.blit(self.image_copy, self.image_rect)

    def update(self):
        """Update the bullets position on screen and slow down the game slightly to simulate recoil."""
        self.i = 0
        self.i += 1
        print(f"i = {self.i}")
        self.image_rect.move_ip(self.vec_x/self.settings.bullet_speed, self.vec_y/self.settings.bullet_speed)
        print(self.vec_x, self.vec_y)