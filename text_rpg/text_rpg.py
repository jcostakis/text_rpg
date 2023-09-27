"""
text_rpg

This module will be the entry point for the game and for now will contain the main loop.

TODO: add typing
"""

from game_ui import GameUI

def main():
    """Contains the main game loop"""

    # Initialize the game user interface
    game_ui = GameUI()

    running = True

    while running:
        # Get and process new events
        new_events = game_ui.poll_events()
        for event in new_events:
            if event == "quit":
                running = False
                break
        
        if not running:
            break

        # Update the view
        game_ui.update() 

    # Clean up
    game_ui.quit()


if __name__ == "__main__":
    main()