"""The ui for the game.

This module is the default user interface for the game. Following the MVC pattern 
(as the view) it is responsible for capturing input and displaying the state
of the game to the user. After creation clients should primarily use this 
class through the update() and publish_events() methods.
"""

import pygame
import pygame_gui
import pygame_gui.core.ui_container

import events.base_event
import events.io_events
import events.system_events
from event_manager import EventManager

CENTRAL_PANEL_PER = 0.7
VIEWPORT_HEIGHT_PER = 0.9
TEXT_INPUT_PX = 50

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
        self.screen_resolution = (1280, 720)
        self._screen: pygame.Surface = pygame.display.set_mode(self.screen_resolution)
        self._ui_manager: pygame_gui.UIManager = pygame_gui.UIManager(self.screen_resolution)
        self._clock: pygame.Clock = pygame.time.Clock()

        # Make UI containers 
        self._main_viewport: pygame_gui.core.ui_container.UIContainer = (
            self.initialize_main_viewport()
        )

        # Initialize the various UI components
        self._output_textbox: pygame_gui.elements.UITextBox = (
            self.initialize_output_textbox(self._main_viewport)
        )
        self._input_textbox: pygame_gui.elements.UITextEntryLine = (
            self.initialize_input_textbox(self._main_viewport)
        )

    def initialize_main_viewport(self) -> pygame_gui.core.ui_container.UIContainer:
        """Creates and returns the main viewport UIContainer.
        
        Returns a UIContainer that is centered along x in the root container and offset from the top 
        based on the VIEWPORT_HEIGHT_PER. Should contain the main text input and output boxes. Sized based
        on VIEWPORT_HEIGHT_PER and CENTRAL_PANEL_PER.
        """
        top_offset = self.screen_resolution[1] * (1 - VIEWPORT_HEIGHT_PER)
        horz_offset = self.screen_resolution[0] * (1 - CENTRAL_PANEL_PER)

        main_viewport_rect = pygame.Rect(0, top_offset, self.screen_resolution[0] - horz_offset, self.screen_resolution[1] - top_offset)
        main_viewport = pygame_gui.core.UIContainer(main_viewport_rect, 
            manager=self._ui_manager, 
            anchors={
                'centerx':'centerx',
                'top': 'top'
            }
        )
        return main_viewport

    def initialize_output_textbox(self, container: pygame_gui.core.ui_container.UIContainer) -> pygame_gui.elements.UITextBox:
        """Creates and returns a read-only UITextBox.

        This returns a textbox that the user can't type text into. Scaled to match the container offset from the bottom by 50 px.
        """
        text_output_rect = pygame.Rect(0, 0, container.get_size()[0], container.get_size()[1] - TEXT_INPUT_PX)
        output_textbox = pygame_gui.elements.UITextBox("", text_output_rect, container=container)
        return output_textbox

    def initialize_input_textbox(self, container: pygame_gui.core.ui_container.UIContainer) -> pygame_gui.elements.UITextEntryLine:
        """Creates and returns a text entry box.

        This returns a text entry box that will accept user input. It is scaled horizontally to match the continer and 50 px tall.
        """
        text_input_rect = pygame.Rect(0, -TEXT_INPUT_PX, container.get_size()[0], TEXT_INPUT_PX)

        input_textbox = pygame_gui.elements.UITextEntryLine(
            text_input_rect, self._ui_manager, initial_text="> ", container=container,
                    anchors={
                        'bottom': 'bottom'
                    }
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
