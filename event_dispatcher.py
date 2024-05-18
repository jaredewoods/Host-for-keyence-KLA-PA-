# event_dispatcher.py


class EventDispatcher:
    def __init__(self):
        self.handlers = {}
        self.values = {}

    def register_event(self, event_name, handler):
        print(f'Registered event: {event_name}')
        if event_name not in self.handlers:
            self.handlers[event_name] = []
        self.handlers[event_name].append(handler)

    def emit(self, event_name, *args, **kwargs):
        print(f'Emitting event: {event_name}')
        for handler in self.handlers.get(event_name, []):
            handler(*args, **kwargs)

    def set(self, key, value):
        self.values[key] = value

    def get(self, key, default=None):
        return self.values.get(key, default)
