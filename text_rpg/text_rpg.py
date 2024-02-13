"""The entry point for the game.

The main loop is ran in this module, however most logic should be handled by 
other components. The responsibility of this module is to begin the program, 
and tell the components to do whatever work they need to do each loop. Specific
logic for how the game should work should be delegated to other modules such as
controllers like the event manager.
"""

from event_manager import EventManager
from game_state_manager import GameStateManager
from game_ui import GameUI

def main() -> None:
    """Initializes the game's components and runs the main loop"""

    # Initialize controller modules
    event_manager = EventManager()
    game_state_manager = GameStateManager(event_manager)

    # Initialize the game user interface
    game_ui = GameUI(event_manager)

    while True:
        # Handle events
        game_ui.publish_events()
        event_manager.process_events()

        if not game_state_manager.is_running:
            break

        # Any other updates go here

        # Update the view
        game_ui.update()


if __name__ == "__main__":
    main()
