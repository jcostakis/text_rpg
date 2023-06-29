"""
text_rpg

This module will be the entry point for the game and for now will contain the main loop.
"""
import pygame

if __name__ == "__main__":
    # Set up 
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True

    # Game loop
    while running:
        # Process events
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    running = False

        # Update
        # Do i get pressed keys here or in processing events?

        # Render 
        # Wipe away previous frame
        screen.fill("purple") 
        pygame.display.flip()

        clock.tick(60) # Limit fps

    # Quit game
    pygame.quit()