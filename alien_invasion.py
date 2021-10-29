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
            self.ship.update()

            # Redraw the screen during each pass through the loop.
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if True:
                print("event.type is " + self.evt_type_str(event.type))
                
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type ==pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

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
        elif event_type == pygame.KEYUP:
            result = "KEYUP"
        else:
            result = "DUNNO TYPE " + str(event_type)

        return result

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()

    
