class EventDispatcher:
    def __init__(self):
        self.handlers = {}

    def register_event(self, event_name, handler):
        print(f'Registered event: {event_name}')
        if event_name not in self.handlers:
            self.handlers[event_name] = []
        self.handlers[event_name].append(handler)

    def emit(self, event_name, *args, **kwargs):
        print(f'Emitting event: {event_name}')
        for handler in self.handlers.get(event_name, []):
            handler(*args, **kwargs)
