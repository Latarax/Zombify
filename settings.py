import pygame

class Settings:
    """Class that stores settings for the game."""
    def __init__(self):
        self.width = 1280 
        self.height = 720
        self.color = (230, 230, 230)
        self.speed = 3
        self.bullets_allowed = 1
        self.bullet_available = True
        self.bullet_speed = 20
        self.zombie_speed = 0.25
        