import pygame
import math
from time import sleep

class Survivor:
    """
    Class for the main character of the game which manages current instance of character.
    """
    def __init__(self, current_game):
        """
        Takes in current instance of game and initializes survivor's attributes.
        """
        # Load main character image and set the rect and starting position
        self.screen = current_game.screen
        self.settings = current_game.settings
        self.image = pygame.image.load('images/ship.bmp')
        self.image_copy = pygame.image.load('images/ship.bmp')
        self.screen_rect = current_game.screen_rect
        self.image_rect = self.image.get_rect()
        self.image_rect.midbottom = current_game.screen_rect.midbottom
        
        # Movement flags and increment variables
        self.moving_right = False
        self.moving_left = False
        self.is_jumping = False
        self.slow_mo = False
        self.slow_mo_available = True
        self.jump_count = 10

    def update_survivor(self):
        """Moves survivor according to keystrokes and mouse movement."""
        self._mouse_rotation()
        # Rightward movement
        if self.moving_right and self.image_rect.right < self.screen_rect.right:
            self.image_rect.x += self.settings.speed
        # Leftward movement
        if self.moving_left and self.image_rect.left > self.screen_rect.left:
            self.image_rect.x -= self.settings.speed
        # Jumping
        if self.is_jumping:
            self._jump()
        if self.slow_mo and self.slow_mo_available:
            pygame.time.delay(20)
            #self.slow_mo = False
            #self.slow_mo_available = False
            
    def _jump(self):
        """Moves survivor upward and downward in a jumping motion."""
        # Slows down jump and adjusts movement variables accordingly
        pygame.time.delay(10)
        self.settings.speed = 9
        self.settings.bullet_speed = 5
        self.settings.zombie_speed = 0.75
        if self.jump_count >= -10:
            up_down = 1
            if self.jump_count < 0:
                up_down = -1
            # Quadratic formula to calculate upward and downward velocity
            self.image_rect.y -= (self.jump_count ** 2)* 0.25 * up_down
            self.jump_count -= 0.3
        else:
            # Assigns variables back to pre jump values
            self.is_jumping = False
            self.jump_count = 10
            self.image_rect.bottom = self.screen_rect.bottom
            self.settings.speed = 3
            self.settings.bullet_speed = 20
            self.settings.zombie_speed = 0.25

    def _mouse_rotation(self):
        """"Aims the survivor's gun to the mouse's current position."""
        mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
        self.survivor_x = mouse_pos_x - self.image_rect.x
        self.survivor_y = mouse_pos_y - self.image_rect.y
        self.angle = math.degrees(math.atan2(self.survivor_x, self.survivor_y))
        self.image_copy = pygame.transform.rotate(self.image, int(self.angle + 180))
        self.image_rect = self.image_copy.get_rect(midbottom = self.image_rect.midbottom)


            
            