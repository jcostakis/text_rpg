"""
text_rpg

This module will be the entry point for the game and for now will contain the main loop.

TODO: add typing
"""
import pygame

class TextInput:
    """The UI element where the player will input their commands

    Will handle keypresses when active.
    """
    def __init__(self):
        """Active is false and contents are empty upon creation.
        """
        self.active = False
        self.contents = ""

    def handle_keypress(self, keypress):
        """Handles keypress by the player if it is currently active
        
        keypress: a string representing the player's keypress 
        """
        self.contents += keypress
        print(self.contents)
        pass

if __name__ == "__main__":
    # Set up 
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True

    # Create UI elements
    command_line = TextInput()

    # Game loop
    while running:
        # Process events
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    running = False
                case pygame.TEXTINPUT:
                    print("success")
                    command_line.handle_keypress(event.unicode)

        # Update
        # Do i get pressed keys here or in processing events?

        # Render 
        # Wipe away previous frame
        screen.fill("purple") 
        pygame.display.flip()

        clock.tick(60) # Limit fps

    # Quit game
    pygame.quit()