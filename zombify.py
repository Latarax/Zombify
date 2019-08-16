import pygame
import sys
import time
from settings import Settings
from survivor import Survivor
from bullet import Bullet
from zombie import Zombie

class Zombify:
    """Class that manages game's overall functionality."""
    def __init__(self):
        """Constructor function"""
        # Initialize the pygame module, class instances, and screen/screen_rect size
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.width,                 self.settings.height))
        self.screen_rect = self.screen.get_rect()
        self.survivor = Survivor(self)
        self.zombies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self._add_zombie()
        self.slow_mo_reload_event = pygame.USEREVENT + 1
        self.spawn_enemy = pygame.USEREVENT + 2
        pygame.time.set_timer(self.slow_mo_reload_event, 5000)
        pygame.time.set_timer(self.spawn_enemy, 5000)

        self.myFont = pygame.font.SysFont("Times New Roman", 18)
        
    def run_game(self):
        """Runs main loop for the game"""         
        # Main loop for the game
        while 1:
            self._event_handler()          
            self.survivor.update_survivor()
            self.bullets.update()
            self.zombies.update(self)
            self._remove_bullets()
            self._update_screen()

    def _update_screen(self):
        """Draw and update the screen"""
        self.screen.fill(self.settings.color)            
        self.screen.blit(self.survivor.image_copy, self.survivor.image_rect)
        #self.screen.blit(self.zombie.image, self.zombie.image_rect)
        self._onscreen_text()
        self.screen.blit(self.label1, (self.screen_rect.left+20, self.screen_rect.top+20))
        self.screen.blit(self.label2, (self.screen_rect.left+170, self.screen_rect.top+20))
        self.screen.blit(self.label3, (self.screen_rect.right-175, self.screen_rect.top+20))
        self.screen.blit(self.label4, (self.screen_rect.right-50, self.screen_rect.top+20))
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
                    
        #self.zombies.draw(self.screen)
        for zombie in self.zombies.sprites():
            zombie.draw_zombie()

        pygame.display.flip()
        
        

    def _add_bullet(self):
        """Adds bullet to screen."""
        # Makes sure there is no more than one bullet on screen
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            self.settings.bullet_available = False
    
    def _add_zombie(self):
        """Adds zombie to screen."""
        zombie = Zombie(self)
        self.zombies.add(zombie)
    
    def _remove_bullets(self):
        """Removes bullet object if it leaves bounds of the screen."""
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= self.screen_rect.top or bullet.rect.right <= self.screen_rect.left or bullet.rect.top >= self.screen_rect.bottom or bullet.rect.left >= self.screen_rect.right:
                self.bullets.remove(bullet)
                self.settings.bullet_available = True
        
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.zombies, True, True) 
        #print(len(self.bullets))

    def _event_handler(self):
        """Manages events such as keystrokes or mouse clicks."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == self.slow_mo_reload_event:
                self.survivor.slow_mo_available = True
            elif event.type == self.spawn_enemy:
                self._add_zombie()
            # Handles events when key is pressed
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    sys.exit()
                if event.key == pygame.K_d:
                    self.survivor.moving_right = True
                if event.key == pygame.K_a:
                    self.survivor.moving_left = True
                if event.key == pygame.K_SPACE or event.key == pygame.K_w:
                    self.survivor.is_jumping = True
                if event.key == pygame.K_LSHIFT:
                    self.survivor.slow_mo = True
                    #self.test = pygame.get_ticks()

            # Handles events when key is released            
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    self.survivor.moving_right = False
                if event.key == pygame.K_a:
                    self.survivor.moving_left = False
                if event.key == pygame.K_LSHIFT:
                    self.survivor.slow_mo = False
                    self.survivor.slow_mo_available = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self._add_bullet()

    def _onscreen_text(self):
        """Renders text onto player's screen"""
        self.label1 = self.myFont.render("Slow-Mo Available: ", 1, (0,0,0))
        
        if self.survivor.slow_mo_available:
            self.label2 = self.myFont.render(f"{self.survivor.slow_mo_available}", 1, (0,200,0))
        else:
            self.label2 = self.myFont.render(f"{self.survivor.slow_mo_available}", 1, (200,0,0))

        self.label3 = self.myFont.render("Bullet Available: ", 1, (0,0,0))
        
        if self.settings.bullet_available:
            self.label4 = self.myFont.render(f"{self.settings.bullet_available}", 1, (0,200,0))
        else:
            self.label4 = self.myFont.render(f"{self.settings.bullet_available}", 1, (200,0,0))



if __name__ == '__main__':
    zombify = Zombify()
    zombify.run_game()
    
