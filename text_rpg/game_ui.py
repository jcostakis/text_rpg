"""The ui for the game.

This module is the default user interface for the game. Following the MVC pattern 
(as the view) it is responsible for capturing input and displaying the state
of the game to the user. After creation clients should primarily use this 
class through the update() and publish_events() methods.
"""

import pygame
import pygame_gui

import events.base_event
import events.io_events
import events.system_events
from event_manager import EventManager


class GameUI:
    """The UI component of the game.

    This class is responsible for displaying the game's state and publishing user
    input events to the event_manager.
    """

    def __init__(self, event_manager: EventManager) -> None:
        self._event_manager: EventManager = event_manager

        # Register as a listener to relevent events
        self._event_manager.register_listener(self, events.system_events.QuitEvent)
        self._event_manager.register_listener(self, events.io_events.TextOutputChanged)

        pygame.init()

        # Initialize pygame and pygame_gui core components
        screen_resolution = (1280, 720)
        self._screen: pygame.Surface = pygame.display.set_mode(screen_resolution)
        self._ui_manager: pygame_gui.UIManager = pygame_gui.UIManager(screen_resolution)
        self._clock: pygame.Clock = pygame.time.Clock()

        # Initialize the various UI components
        self._output_textbox: pygame_gui.elements.UITextBox = (
            self.initialize_output_textbox()
        )
        self._input_textbox: pygame_gui.elements.UITextEntryBox = (
            self.initialize_input_textbox()
        )

    def initialize_output_textbox(self) -> pygame_gui.elements.UITextBox:
        """Creates and returns a read-only UITextBox.

        This returns a 300x300 px textbox that the user can't type text into
        directly.
        """
        text_output_rect = pygame.Rect(0, 0, 300, 300)
        output_textbox = pygame_gui.elements.UITextBox("", text_output_rect)
        return output_textbox

    def initialize_input_textbox(self) -> pygame_gui.elements.UITextEntryLine:
        """Creates and returns a text entry box.

        This returns a 300x100 px text entry box that will accept user input.
        """
        text_input_rect = pygame.Rect(0, 300, 300, 100)
        input_textbox = pygame_gui.elements.UITextEntryLine(
            text_input_rect, self._ui_manager, initial_text="> "
        )
        return input_textbox

    def update(self) -> None:
        """Redraws the GUI so that any graphical changes are displayed.

        Updates to components directly should not occur here. They should result
        from handle_event calls through the event_manager. (For example, if new
        text is entered by the user it should generate an event which a text
        box is listening to and then the text box should append that text.)
        """
        # Tick returns the time in milliseconds since last frame, divide by 1000 to convert to seconds
        time_delta = self._clock.tick(60) / 1000.00
        self._ui_manager.update(time_delta)

        # Set background color
        self._screen.fill("purple")

        # Update UI elements
        self._ui_manager.draw_ui(self._screen)
        pygame.display.flip()

    def quit(self) -> None:
        """Close the GUI window for application shutdown."""
        pygame.quit()

    def publish_events(self) -> None:
        """Publish events based on UI interactions.

        All events produced by the GUI should be published for the event system
        here so that any listeners can perform the necessary logic in response
        to that event.
        """
        for event in pygame.event.get():
            self._ui_manager.process_events(event)
            match event.type:
                case pygame.QUIT:
                    self._event_manager.queue_event(events.system_events.QuitEvent())
                case pygame_gui.UI_TEXT_ENTRY_FINISHED:
                    self._event_manager.queue_event(
                        events.io_events.TextInputEvent(event.text)
                    )
                    self._input_textbox.set_text("> ")

    def handle_event(self, event: events.base_event.BaseEvent) -> None:
        match event:
            case events.system_events.QuitEvent():
                self.quit()
            case events.io_events.TextOutputChanged():
                self._output_textbox.set_text(event.output_text)
