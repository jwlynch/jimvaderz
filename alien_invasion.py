import sys

import pygame

from  settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for kleybopard and mouse events.
            self._check_events()

            # Redraw the screen during each pass through the loop.
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if False:
                print("event.type is " + self.evt_type_str(event.type))
                
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

    def evt_type_str(self, event_type):
        if event_type == pygame.QUIT:
            result = "QUIT"
        elif event_type == pygame.KEYDOWN:
            result = "KEYDOWN"
        else:
            result = "DUNNO TYPE"

        return result

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()

    
