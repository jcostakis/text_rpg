"""Responsible for managing all behavior related to using the event system.

All behavior related to the functioning of events should be located in this
module unless this module becomes significantly more complicated in the future.
This includes adding and removing listeners for events and notifying listeners
of events when the queue is processed. 
"""

from collections import deque
from typing import Type

from events.base_event import BaseEvent


class EventManager:
    """Tracks listeners for events and notifies listeners when those events
    are processed

    In order for a component to be responsive to events occuring in the program
    it should be registered as a listener to the relevent event type that the
    component should do something in response to. Before that component is
    deleted it should unregister as a listener.
    """

    def __init__(self) -> None:
        # Maps from event types to listeners of that event type
        self._listeners: dict[Type[BaseEvent], list[object]] = {}
        self._event_queue: deque[BaseEvent] = deque()

    def register_listener(self, listener: object, event_type: Type[BaseEvent]) -> None:
        """Adds a listener for the given event_type.

        Args:
            listener:
                The object that will be notified when that type of event occurs.
            event_type:
                The type of event that the listener will be notified of.

        Raises:
            ValueError: The listener doesn't have a handle_event method.
        """
        if not hasattr(listener, "handle_event"):
            raise ValueError(
                f"{type(listener).__name__} doesn't have a handle_event method."
            )
        self._listeners.setdefault(event_type, []).append(listener)

    def unregister_listener(
        self,
        listener: object,
        event_type: Type[BaseEvent],
    ) -> None:
        """Removes a listener for the given event_type.

        Args:
            listener:
                The object that will no longer be listening to the event type.
            event_type:
                The type of event that the listener will no longer be notified of.
        """
        if event_type in self._listeners and listener in self._listeners[event_type]:
            self._listeners[event_type].remove(listener)

    def queue_event(self, event: BaseEvent) -> None:
        """Adds an event to the queue to be processed next process_events call.

        Args:
            event:
                The event that will be queued.
        """
        if not isinstance(event, BaseEvent):
            raise ValueError(f"{type(event).__name__} is not an event!")
        self._event_queue.append(event)

    def notify(self, event: BaseEvent) -> None:
        """Immediately notify all relevant listeners of the current event.

        Args:
            event:
                The event that listeners will be notified of.
        """
        type_listeners = self._listeners.get(type(event), [])
        for listener in type_listeners:
            listener.handle_event(event)

    def process_events(self) -> None:
        """Processes all events in the event_queue, leaving it empty."""
        # Note that this will process events that are created while processing old events
        while self._event_queue:
            self.notify(self._event_queue.popleft())
