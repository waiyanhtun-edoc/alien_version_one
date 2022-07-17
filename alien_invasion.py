import imp
import sys
import pygame
from settings import Settings
from ship import Ship
from background import Background

class AlienInvasion:
    """Overall class to manage game assets and behavior."""
    
    def __init__(self):
        """Initialie the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        #set the game screen size
        self.screen = pygame.display.set_mode((
                self.settings.screen_width,self.settings.screen_height))
        self.ship = Ship(self)
        self.background = Background(self)


    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_event()
            self._update_screen()

            
    def _check_event(self):
        """Check the game event """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    
    def _update_screen(self):
        """Update the screen everything"""
        #set background color
        self.screen.fill(self.settings.bg_color)
        #set background img
        self.background.blitBack()
        #Draw thd ship here 
        self.ship.blitme()
        #Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()