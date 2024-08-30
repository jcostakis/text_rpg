"""This module is responsible for handling text output. 

It is responsible for managing the text_output model and updating the output so 
that it reflects the current game state. Formatting, text output modes, and 
changes to the text_output model are responsiblities of this module.
"""

from text_output import TextOutput
from events import base_event, io_events
from event_manager import EventManager


class TextOutputHandler:
    """Handles text input by updating the text_output and passing text to the parser."""

    def __init__(self, event_manager: EventManager):
        # Initialize components
        self.event_manager = event_manager
        self.text_output: TextOutput = TextOutput(event_manager)

        self.event_manager.register_listener(self, io_events.TextInputEvent)
        self.event_manager.register_listener(self, io_events.ClearOutputRequest)
        self.event_manager.register_listener(self, io_events.PrintToOutput)

    def handle_event(self, event: base_event.BaseEvent):
        match event:
            case io_events.TextInputEvent():
                self.text_output.append_line(event.input_text)
            case io_events.ClearOutputRequest():
                self.text_output.clear()
            case io_events.PrintToOutput():
                self.text_output.append_line(event.print_text)
