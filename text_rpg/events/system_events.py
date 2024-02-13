"""Contains events related to general system behavior."""

from events.base_event import BaseEvent


class QuitEvent(BaseEvent):
    """There is a request to quit."""
