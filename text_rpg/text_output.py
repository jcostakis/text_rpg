""""This module is the model for the text output of the game."""

from event_manager import EventManager
from events.io_events import TextOutputChanged


class TextOutput:
    """Maintains and contains the text output history of the game."""

    def __init__(self, event_manager: EventManager) -> None:
        self.event_manager: EventManager = event_manager
        self.text: str = ""

    def clear(self) -> None:
        """Clears text output."""
        self.text: str = ""
        self.event_manager.queue_event(TextOutputChanged(self.text))

    def append_line(self, new_text: str) -> None:
        """Append a new line of text to the output."""
        self.text += new_text + "\n"
        self.event_manager.queue_event(TextOutputChanged(self.text))
