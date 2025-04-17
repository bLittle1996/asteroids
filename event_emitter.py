from collections.abc import Callable
from typing import Any, Self


type Event = str | int
type EventListener = Callable[[Any], Any]

class EventEmitter:
    default: Self

    def __init__(self) -> None:
        self.listeners: dict[Event, list[EventListener]] = {}

    def on(self, event: Event, listener: EventListener) -> None:
        event_listeners = self.listeners.get(event)
        if event_listeners != None:
            event_listeners.append(listener)
        else:
            self.listeners[event] = [listener]

    def off(self, event: Event, listener: EventListener) -> None:
        event_listeners = self.listeners.get(event)

        if event_listeners == None:
            return

        event_listeners.remove(listener)

    def emit(self, event: Event, payload: Any) -> None:
        event_listeners = self.listeners.get(event)

        if event_listeners == None:
            return

        for listener in event_listeners:
            listener(payload)


EventEmitter.default = EventEmitter()
