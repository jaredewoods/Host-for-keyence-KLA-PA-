# event_dispatcher.py
def register_events(dispatcher, serial_service, tcp_service, macro_service, log_to_display, clear_log_display, scan_com_ports, quit_application, update_serial_connection_status, update_tcp_connection_status, update_macro_running_status, update_completed_cycles_display):
    print("Registering Events")
    dispatcher.register_event('connectSerialPort', serial_service.connect_serial_port)
    dispatcher.register_event('closeSerialPort', serial_service.close_serial_port)
    dispatcher.register_event('moveToReadyStation', serial_service.move_to_ready_station)
    dispatcher.register_event('alignWafer', serial_service.align_wafer)
    dispatcher.register_event('chuckHold', serial_service.chuck_hold)
    dispatcher.register_event('hardwareReset', serial_service.hardware_reset)
    dispatcher.register_event('sendCustomSerial', serial_service.send_custom_serial)
    dispatcher.register_event('emergencyStop', serial_service.emergency_stop)
    dispatcher.register_event('sendClearCommand', serial_service.send_clear_command)

    dispatcher.register_event('connectTCP', tcp_service.connect_tcp_socket)
    dispatcher.register_event('disconnectTCP', tcp_service.close_tcp_socket)
    dispatcher.register_event('triggerOne', tcp_service.trigger_one)
    dispatcher.register_event('triggerTwo', tcp_service.trigger_two)
    dispatcher.register_event('prevCamera', tcp_service.prev_camera)
    dispatcher.register_event('nextCamera', tcp_service.next_camera)
    dispatcher.register_event('sendCustomTCP', tcp_service.send_custom_tcp)

    dispatcher.register_event('stopSequence', macro_service.stop_sequence)
    dispatcher.register_event('initializeSequence', macro_service.initialize_sequence)
    dispatcher.register_event('startSequence', macro_service.initialize_sequence)
    dispatcher.register_event('resetSequence', macro_service.reset_sequence)
    dispatcher.register_event('sendCommandMTRS', macro_service.send_command_mtrs)
    dispatcher.register_event('handleResponseMTRS', macro_service.handle_response_mtrs)
    dispatcher.register_event('sendCommandMALN', macro_service.send_command_maln)
    dispatcher.register_event('handleResponseMALN', macro_service.handle_response_maln)
    dispatcher.register_event('sendCommandT1', macro_service.send_command_t1)
    dispatcher.register_event('handleResponseT1', macro_service.handle_response_t1)
    dispatcher.register_event('incrementCycleCount', macro_service.increment_cycle_count)
    dispatcher.register_event('emergencyStop', macro_service.emergency_stop_sequence)

    dispatcher.register_event('logToDisplay', log_to_display)
    dispatcher.register_event('receivedData', log_to_display)
    dispatcher.register_event('clearLogDisplay', clear_log_display)

    dispatcher.register_event('scanForSerialPorts', scan_com_ports)
    dispatcher.register_event('quitApplication', quit_application)

    dispatcher.register_event('updateSerialConnectionStatus', update_serial_connection_status)
    dispatcher.register_event('updateTCPConnectionStatus', update_tcp_connection_status)
    dispatcher.register_event('updateMacroRunningStatus', update_macro_running_status)
    dispatcher.register_event('updateCompletedCycles', update_completed_cycles_display)


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
