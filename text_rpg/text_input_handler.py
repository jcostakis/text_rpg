"""This module is responsible for handling text_input.

It passes input text to the text_parser and manipulates the text_output
model so that it reflects the current game state.

TODO: Probably rename this if the responsibilities change?
"""

from text_output import TextOutput
from text_parser import TextParser
from events import base_event, io_events
from event_manager import EventManager


class TextInputHandler:
    """Handles text input by updating the text_output and passing text to the parser."""

    def __init__(self, event_manager: EventManager):
        # Initialize components
        self.event_manager = event_manager
        self.text_output: TextOutput = TextOutput(event_manager)
        self.text_parser: TextParser = TextParser(event_manager)

        self.event_manager.register_listener(self, io_events.TextInputEvent)
        self.event_manager.register_listener(self, io_events.ClearOutputRequest)

    def handle_event(self, event: base_event.BaseEvent):
        match event:
            case io_events.TextInputEvent():
                self.text_parser.handle_input(event.input_text)
                self.text_output.append_line(event.input_text)
            case io_events.ClearOutputRequest():
                self.text_output.clear()
