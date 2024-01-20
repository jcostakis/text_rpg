"""Serves as the base event class for all other events.

TODO:
    - Add support for timezones
"""

import datetime
import uuid 

class BaseEvent():
    """Base event class that all other events should inherit."""

    def __init__(self):
        self.id: uuid.UUID = uuid.uuid4()
        self.timestamp: datetime.datetime = datetime.datetime.now()

    def __str__(self):
        return f"{self.__class__.__qualname__} {self.id} at {self.timestamp}"
