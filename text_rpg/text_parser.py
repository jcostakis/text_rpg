import enum

from event_manager import EventManager
from events.io_events import ClearOutputRequest
from events.system_events import QuitEvent

class Tokens(enum.Enum):
    CLEAR = 1
    ERROR = 2
    QUIT = 3


class TextParser:

    def __init__(self, event_manager: EventManager):
        self.event_manager: EventManager = event_manager

    def handle_input(self, input_string: str) -> None:
        tokens = self.tokenize(input_string)
        if len(tokens) == 1: 
            match tokens[0]:
                case Tokens.CLEAR:
                    self.event_manager.queue_event(ClearOutputRequest())
                case Tokens.QUIT:
                    self.event_manager.queue_event(QuitEvent())
            

    def tokenize(self, string: str) -> list[Tokens]:
        tokens = []

        # Get rid of input prompt:
        string = string.removeprefix(">")

        words = string.split()
        for word in words:
            match word.lower():
                case "clear":
                    tokens.append(Tokens.CLEAR)
                case "quit" | "exit":
                    tokens.append(Tokens.QUIT)
                case _:
                    tokens.append(Tokens.ERROR)

        return tokens
