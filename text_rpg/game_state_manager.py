"""Component responsible for transitioning between game states.

This module will contain logic for tranistioning between game states
such as pausing, menu transitions, quiting, saving, etc. It should
be referenced for checking what state the game is in.
"""

from events.base_event import BaseEvent
from event_manager import EventManager

import events.system_events


class GameStateManager:
    """Responsible for transitioning between game states.

    Attributes:
        is_running: Bool that states whether the game is terminating.
        event_manager: The global event manager that notifies the class of events.
    """

    def __init__(self, event_manager: EventManager) -> None:
        self.is_running: bool = True

        self.event_manager: EventManager = event_manager
        self.event_manager.register_listener(self, events.system_events.QuitEvent)

    def handle_event(self, event: BaseEvent) -> None:
        if isinstance(event, events.system_events.QuitEvent):
            self.is_running = False
