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

    # Create text box for displaying descriptive text
    text_box_rect = pygame.Rect(0, 0, 300, 300)
    text_box = pygame_gui.elements.UITextBox("test", text_box_rect)

    # Create text box for player input
    text_input_rect = pygame.Rect(0, 300, 300, 100)
    text_input = pygame_gui.elements.UITextEntryLine(text_input_rect, manager=manager, initial_text="> ")

    # Game loop
    while running:
        time_delta = clock.tick(60)/1000.00

        # Process events
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    running = False
                case pygame_gui.UI_TEXT_ENTRY_FINISHED:
                    # Append entered text
                    text_box.append_html_text(f"\n{event.text}")
                    text_input.set_text("> ")
            
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