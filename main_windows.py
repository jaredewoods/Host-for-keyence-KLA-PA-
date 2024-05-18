# main_window.py

import sys
import tkinter as tk
from datetime import datetime
from tkinter import ttk, scrolledtext
import serial
import serial.tools.list_ports
from control_frames import SerialControlFrame, TCPControlFrame, MacroControlFrame, StatusFrame
from control_services import SerialService, TCPService, MacroService
from event_dispatcher import EventDispatcher


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.log_display = None
        self.serial_connected = False
        self.tcp_connected = False
        self.macro_running = False
        self.total_cycles = 0
        self.completed_cycles = 0

        print("Initializing MainWindow")
        self.title("Prealigner Vision Repeatability Test")
        self.ntb_control = None
        self.available_ports = []
        self.dispatcher = EventDispatcher()
        self.serial_service = SerialService(dispatcher=self.dispatcher)
        self.tcp_service = TCPService(dispatcher=self.dispatcher)
        self.macro_service = MacroService(dispatcher=self.dispatcher)
        self.scan_com_ports()
        self.create_control_frames()
        self.create_log_frame()
        self.create_status_frame()
        self.register_events()
        self.configure_grid()
        print("MainWindow initialized")

    def register_events(self):
        print("Registering Events")
        self.dispatcher.register_event('connectSerialPort', self.serial_service.connect_serial_port)
        self.dispatcher.register_event('closeSerialPort', self.serial_service.close_serial_port)
        self.dispatcher.register_event('moveToReadyStation', self.serial_service.move_to_ready_station)
        self.dispatcher.register_event('alignWafer', self.serial_service.align_wafer)
        self.dispatcher.register_event('toggleChuck', self.serial_service.toggle_chuck)
        self.dispatcher.register_event('hardwareReset', self.serial_service.hardware_reset)
        self.dispatcher.register_event('sendCustomSerial', self.serial_service.custom_serial_command)

        self.dispatcher.register_event('connectTCP', self.tcp_service.connect_tcp_socket)
        self.dispatcher.register_event('disconnectTCP', self.tcp_service.close_tcp_socket)
        self.dispatcher.register_event('triggerOne', self.tcp_service.trigger_one)
        self.dispatcher.register_event('triggerTwo', self.tcp_service.trigger_two)
        self.dispatcher.register_event('prevCamera', self.tcp_service.prev_camera)
        self.dispatcher.register_event('nextCamera', self.tcp_service.next_camera)
        self.dispatcher.register_event('sendCustomTCP', self.tcp_service.send_custom_tcp)

        self.dispatcher.register_event('stopSequence', self.macro_service.stop_sequence)
        self.dispatcher.register_event('startSequence', self.macro_service.start_sequence)
        self.dispatcher.register_event('stepSequence', self.macro_service.step_sequence)
        self.dispatcher.register_event('resetSequence', self.macro_service.reset_sequence)
        self.dispatcher.register_event('pauseSequence', self.macro_service.pause_sequence)
        self.dispatcher.register_event('continueSequence', self.macro_service.run_sequence)

        self.dispatcher.register_event('logData', self.log_to_display)
        self.dispatcher.register_event('receivedData', self.log_to_display)

        self.dispatcher.register_event('scanForSerialPorts', self.scan_com_ports)
        self.dispatcher.register_event('quitApplication', self.quit_application)
        self.dispatcher.register_event('emergencyStop', self.emergency_stop)

        self.dispatcher.register_event('updateSerialConnectionStatus', self.update_serial_connection_status)
        self.dispatcher.register_event('updateTCPConnectionStatus', self.update_tcp_connection_status)
        self.dispatcher.register_event('updateMacroRunningStatus', self.update_macro_running_status)
        self.dispatcher.register_event('updateCycleCount', self.update_cycle_count)

    def scan_com_ports(self):
        print("Scanning Ports")
        ports = [port.device for port in serial.tools.list_ports.comports()]
        print(f"Available Ports: {ports}")
        self.available_ports = ports
        return ports

    def configure_grid(self):
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)  # Makes column 1 resizable
        self.grid_rowconfigure(0, weight=1)     # Makes row 0 resizable

    def create_control_frames(self):
        print("Creating Control Frames")
        self.ntb_control = ttk.Notebook(self)
        self.ntb_control.grid(row=0, column=0, sticky="", padx=10, pady=(10, 0))

        macro_control_tab = ttk.Frame(self.ntb_control)
        macro_control = MacroControlFrame(macro_control_tab, dispatcher=self.dispatcher)
        macro_control.pack(fill=tk.BOTH, expand=True)
        self.ntb_control.add(macro_control_tab, text="  Macro  ")

        serial_control_tab = ttk.Frame(self.ntb_control)
        serial_control = SerialControlFrame(serial_control_tab, self.available_ports, dispatcher=self.dispatcher)
        serial_control.pack(fill=tk.BOTH, expand=True)
        self.ntb_control.add(serial_control_tab, text="  Serial  ")

        tcp_control_tab = ttk.Frame(self.ntb_control)
        tcp_control = TCPControlFrame(tcp_control_tab, dispatcher=self.dispatcher)
        tcp_control.pack(fill=tk.BOTH, expand=True)
        self.ntb_control.add(tcp_control_tab, text="   TCP   ")
        print("Control Frames created.")

    def create_log_frame(self):
        self.log_display = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=60)
        self.log_display.grid(row=0, column=1, rowspan=2, sticky="nsew", padx=5, pady=10)

    def create_status_frame(self):
        self.status_frame = StatusFrame(self, dispatcher=self.dispatcher)
        self.status_frame.grid(row=1, column=0, sticky="", padx=10, pady=5)

    def log_to_display(self, message, source, direction):
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_message = f"[{timestamp}] {source} {message}"
        self.log_display.insert(tk.END, f"{log_message}\n")
        self.log_display.see(tk.END)

    def update_serial_connection_status(self, status):
        self.serial_connected = status
        self.dispatcher.emit('updateButtonStates')

    def update_tcp_connection_status(self, status):
        self.tcp_connected = status
        self.dispatcher.emit('updateButtonStates')

    def update_macro_running_status(self, status):
        self.macro_running = status

    def update_cycle_count(self, total, completed):
        self.total_cycles = total
        self.completed_cycles = completed

    @staticmethod
    def quit_application():
        print("Quitting")
        sys.exit()

    @staticmethod
    def emergency_stop():
        print("Emergency Stop!")


if __name__ == "__main__":
    main_window = MainWindow()
    main_window.mainloop()
