"""
text_rpg

This module will be the entry point for the game and for now will contain the main loop.

TODO: add typing
"""

from event_manager import EventManager
from game_state_manager import GameStateManager
from game_ui import GameUI

def main():
    """Contains the main game loop"""

    # Initialize controller modules
    event_manager = EventManager()
    game_state_manager = GameStateManager(event_manager)

    # Initialize the game user interface
    game_ui = GameUI(event_manager)

    while game_state_manager.is_running:
        game_ui.publish_events()
        event_manager.process_events()
        
        if not game_state_manager.is_running:
            break

        # Update the view
        game_ui.update() 

    # Clean up
    game_ui.quit()

if __name__ == "__main__":
    main()