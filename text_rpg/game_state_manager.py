"""game_state_manager

This module will contain logic for tranistioning between game states
such as pausing, menu transitions, quiting, saving, etc. It should
be referenced for checking when behaviors should be performed.
"""
import events.system_events
from event_manager import EventManager

class GameStateManager():

    def __init__(self, event_manager):
        self.is_running = True

        self.event_manager = event_manager
        self.event_manager.register_listener(events.system_events.QuitEvent, self)
    
    def handle_event(self, event):
        if isinstance(event, events.system_events.QuitEvent):
            self.is_running = False