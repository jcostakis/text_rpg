"""Contains events related to input and output."""

from events.base_event import BaseEvent


class TextInputEvent(BaseEvent):
    """The user entered text.

    Attributes:
        input_text: The text entered by the user without alteration."""

    def __init__(self, input_text: str) -> None:
        self.input_text: str = input_text
        super().__init__()


class TextOutputChanged(BaseEvent):
    """The text output has changed.

    Attributes:
        output_text: The full current str that output text contains."""

    def __init__(self, output_text: str) -> None:
        self.output_text: str = output_text
        super().__init__()


class ClearOutputRequest(BaseEvent):
    """Request to clear the output text."""

class PrintToOutput(BaseEvent):
    """Print text to the output text box.

    Attributes:
        print_text: Text to be printed by the output text box."""

    def __init__(self, print_text: str) -> None:
        self.print_text : str = print_text 
        super().__init__()