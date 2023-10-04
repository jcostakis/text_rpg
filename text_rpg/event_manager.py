from typing import Type

from base_event import BaseEvent
# TODO: Should I be importing like this instead of just importing the module?

class EventManager():
    """Responsible for keeping track of listeners and relaying messages to them
    """
    def __init__(self):
        self.listeners: Dict[Type[BaseEvent], List[object]] = {}
        self.event_queue: List[BaseEvent] = []

    def register_listener(self, event_type: Type[BaseEvent], listener: object):
        """Adds a listener to the given event_type"""
        if not hasattr(listener, "handle_event"):
            raise ValueError(f"{listener} doesn't have a handle_event method.")
        self.listeners.setdefault(event_type, []).append(listener)

    def unregister_listener(self, event_type: Type[BaseEvent], listener: object):
        """Removes a listener to the given event_type"""
        if event_type in self.listeners and listener in self.listeners[event_type]:
                self.listeners[event_type].remove(listener)

    def queue_event(self, event: BaseEvent):
        """Adds an event to the queue to be processed on the next update"""
        self.event_queue.append(event)
    
    def notify(self, event: BaseEvent):
        """Immediately notify all relevant listeners of the current event"""
        for event_type, listeners in self.listeners.items():
            if isinstance(event, event_type):
                for listener in listeners:
                    listener.handle_event(event)

    def process_events(self):
        """Processes all events in the event_queue"""
        while self.event_queue:
            self.notify(self.event_queue.pop())