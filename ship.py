import pygame

class Ship:
    """A class to manage the ship"""

    def __init__(self,game_screen):
        """Initialize the ship and set its starting position."""
        #set thet game_screen background with rect
        self.screen = game_screen.screen
        self.screen_rect = self.screen.get_rect()

        #set the ship image and ship position with rect
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()

        #set each new ship at the bottom of the game_scree
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image,self.rect)
