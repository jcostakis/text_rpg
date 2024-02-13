"""Serves as the base event class for all events types.

Includes basic functionality that is shared among all event types.
"""

import datetime
import uuid


class BaseEvent:
    """Base event class that all other events should inherit.

    Attributes:
        id: The UUID uniquely identifying the event.
        timestamp: The local datetime that the event was generated.
    """

    def __init__(self) -> None:
        self.id: uuid.UUID = uuid.uuid4()
        self.timestamp: datetime.datetime = datetime.datetime.now()

    def __str__(self) -> str:
        return f"{self.__class__.__qualname__} {self.id} at {self.timestamp}"
