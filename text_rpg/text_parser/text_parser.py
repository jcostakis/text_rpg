"""The module that converts user input text into commands and relevant events.

This module is responsible for validating and determining what kind of request
the user is attempting. It will report an error if an invalid input is detected
and otherwise produce an event that will communicate the user's request to the
rest of the game.
"""

import enum

from event_manager import EventManager
from events.io_events import ClearOutputRequest, PrintToOutput
from events.system_events import QuitEvent

class Tokens(enum.Enum):
    """Tokens representing possible inputs by the user."""

    CLEAR = 1
    ERROR = 2
    QUIT = 3
    HELP = 4


# Maps between keywords and valid tokens
TOKEN_MAP = {
    "clear": Tokens.CLEAR,
    "quit": Tokens.QUIT,
    "exit": Tokens.QUIT,
    "help": Tokens.HELP,
}

HELP_TEXT = "\nclear: clear the text output box\nquit: exit the game\nhelp: display some of the available commands\n"


class TextParser:
    """Converts user text input into events that other modules can respond to."""

    def __init__(self, event_manager: EventManager):
        self.event_manager: EventManager = event_manager

    def handle_input(self, input_string: str) -> None:
        """ "Generates events to communicate user requests to system."""
        # Prepare string
        input_string = input_string.removeprefix(">")
        words = input_string.split()
        
        # First word should be keyword 
        token = TOKEN_MAP.get(words[0].lower(), Tokens.ERROR)
 
        # Parse input tokens
        match token:
            case Tokens.CLEAR:
                self.event_manager.queue_event(ClearOutputRequest())
            case Tokens.QUIT:
                self.event_manager.queue_event(QuitEvent())
            case Tokens.HELP:
                self.event_manager.queue_event(PrintToOutput(HELP_TEXT))
            case Tokens.ERROR:
                self.event_manager.queue_event(PrintToOutput(f"Not a valid keyword: '{words[0]}'"))