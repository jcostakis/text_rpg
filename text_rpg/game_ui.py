"""
game_ui

This module is the default user interface for the game. Following the MVC pattern 
(as the view) it is responsible for capturing input and displaying changes
in the model. 
"""

import pygame
import pygame_gui

class GameUI():
    """A pygame GUI object"""
    def __init__(self):
        pygame.init()

        self.screen_resolution = (1280, 720)

        self.screen = pygame.display.set_mode(self.screen_resolution)
        self.manager = pygame_gui.UIManager(self.screen_resolution)
        self.clock = pygame.time.Clock()

        # TODO: Create a container that these will go in

        # Initialize the various UI components
        self.output_textbox = self.initialize_output_textbox()
        self.input_textbox = self.initialize_input_textbox()


    def initialize_output_textbox(self) -> pygame_gui.elements.UITextBox:
        # Create text box for displaying descriptive text
        text_output_rect = pygame.Rect(0, 0, 300, 300)
        output_textbox = pygame_gui.elements.UITextBox("test", text_output_rect)
        return output_textbox 

    def initialize_input_textbox(self) -> pygame_gui.elements.UITextEntryLine:
        # Create text box for player input
        text_input_rect = pygame.Rect(0, 300, 300, 100)
        input_textbox = pygame_gui.elements.UITextEntryLine(text_input_rect, self.manager, initial_text="> ")
        return input_textbox 
    
    def poll_events(self) -> []:
        new_events = []
        for event in pygame.event.get():
            self.manager.process_events(event)
            match event.type:
                case pygame.QUIT:
                    new_events.append("quit")
                case pygame_gui.UI_TEXT_ENTRY_FINISHED:
                    # Append entered text
                    self.output_textbox.append_html_text(f"\n{event.text}")
                    # TODO: Generate event to be handled by controller here
                    self.input_textbox.set_text("> ")

        return new_events

    def update(self) -> None:
        time_delta = self.clock.tick(60)/1000.00
        self.manager.update(time_delta)

        self.screen.fill("purple") 
        self.manager.draw_ui(self.screen)
        pygame.display.flip()

    def quit(self) -> None:
        pygame.quit()