"""This module is responsible for handling text input.

It passes input text to the text_parser, is responsible for managing potential
input modes and logic that is separate from the conversion of tokens into
events. 
"""

from text_parser import TextParser
from events import base_event, io_events
from event_manager import EventManager


class TextInputHandler:
    """Handles text input by passing text to the parser."""

    def __init__(self, event_manager: EventManager):
        # Initialize components
        self.event_manager = event_manager
        self.text_parser: TextParser = TextParser(event_manager)

        self.event_manager.register_listener(self, io_events.TextInputEvent)

    def handle_event(self, event: base_event.BaseEvent):
        match event:
            case io_events.TextInputEvent():
                self.text_parser.handle_input(event.input_text)
