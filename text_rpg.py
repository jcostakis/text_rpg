"""
text_rpg

This module will be the entry point for the game and for now will contain the main loop.

TODO: add typing
"""
import pygame
import pygame_gui

def main():
    """Contains the main game loop"""
    screen_resolution = (1280, 720)

    # Set up 
    pygame.init()
    screen = pygame.display.set_mode(screen_resolution)
    clock = pygame.time.Clock()
    running = True

    manager = pygame_gui.UIManager(screen_resolution)

    hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)), text="Say hello", manager=manager)

    # Game loop
    while running:
        time_delta = clock.tick(60)/1000.00

        # Process events
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    running = False
            
            manager.process_events(event)

        # Update
        # Do i get pressed keys here or in processing events?
        manager.update(time_delta)

        # Render 
        # Wipe away previous frame
        screen.fill("purple") 
        manager.draw_ui(screen)
        pygame.display.flip()

    # Quit game
    pygame.quit()

if __name__ == "__main__":
    main()