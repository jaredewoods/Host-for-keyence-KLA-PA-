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
from event_registry import register_events


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.completed_cycles = None
        self.status_frame = None
        self.log_display = None
        self.serial_connected = False
        self.tcp_connected = False
        self.macro_running = False
        self.completed_cycles_value = tk.IntVar(value=0)
        print("Initializing MainWindow")
        self.title("Prealigner Vision Repeatability Test")
        self.ntb_control = None
        self.available_ports = []
        self.dispatcher = EventDispatcher()
        self.serial_service = SerialService(dispatcher=self.dispatcher)
        self.tcp_service = TCPService(dispatcher=self.dispatcher)
        self.macro_service = MacroService(dispatcher=self.dispatcher, serial_service=self.serial_service)
        self.scan_com_ports()
        self.create_control_frames()
        self.create_log_frame()
        self.create_status_frame()
        self.register_events()
        self.configure_grid()
        print("MainWindow initialized")

    def register_events(self):
        register_events(
            self.dispatcher,
            self.serial_service,
            self.tcp_service,
            self.macro_service,
            self.log_to_display,
            self.clear_log_display,
            self.scan_com_ports,
            self.quit_application,
            self.emergency_stop,
            self.update_serial_connection_status,
            self.update_tcp_connection_status,
            self.update_macro_running_status,
            self.update_completed_cycles_display
        )

    def scan_com_ports(self):
        print("Scanning Ports")
        ports = [port.device for port in serial.tools.list_ports.comports()]
        print(f"Available Ports: {ports}")
        self.available_ports = ports
        return ports

    def configure_grid(self):
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def create_control_frames(self):
        print("Creating Control Frames")
        self.ntb_control = ttk.Notebook(self)
        self.ntb_control.grid(row=0, column=0, sticky="", padx=10, pady=(10, 0))

        serial_control_tab = ttk.Frame(self.ntb_control)
        serial_control = SerialControlFrame(serial_control_tab, self.available_ports, dispatcher=self.dispatcher)
        serial_control.pack(fill=tk.BOTH, expand=True)
        self.ntb_control.add(serial_control_tab, text="Serial")

        tcp_control_tab = ttk.Frame(self.ntb_control)
        tcp_control = TCPControlFrame(tcp_control_tab, dispatcher=self.dispatcher)
        tcp_control.pack(fill=tk.BOTH, expand=True)
        self.ntb_control.add(tcp_control_tab, text="TCP")
        self.ntb_control.bind("<<NotebookTabChanged>>", self.on_tab_change)
        print("Control Frames created.")

        macro_control_tab = ttk.Frame(self.ntb_control)
        macro_control = MacroControlFrame(macro_control_tab, dispatcher=self.dispatcher,
                                          completed_cycles_value=self.completed_cycles_value)
        macro_control.pack(fill=tk.BOTH, expand=True)
        self.ntb_control.add(macro_control_tab, text=" Macro ")

    def create_log_frame(self):
        self.log_display = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=60)
        self.log_display.grid(row=0, column=1, rowspan=2, sticky="nsew", padx=5, pady=10)

    def clear_log_display(self):
        self.log_display.delete('1.0', tk.END)
        print("Log Display cleared")

    def create_status_frame(self):
        self.status_frame = StatusFrame(self, dispatcher=self.dispatcher)
        self.status_frame.grid(row=1, column=0, sticky="", padx=10, pady=5)

    def log_to_display(self, message, source, direction=None):
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
        print(f'macro running status: {status}')

    def update_completed_cycles_display(self, completed_cycles):
        print(f"Updating completed cycles value MW: {completed_cycles}")
        self.completed_cycles_value.set(completed_cycles)
        print(f"New value in IntVar: {self.completed_cycles_value.get()}")
        self.update_idletasks()

    @staticmethod
    def quit_application():
        print("Quitting")
        sys.exit()

    @staticmethod
    def emergency_stop():
        print("Emergency Stop!")

    def on_tab_change(self, event):  # forces immediate update
        self.ntb_control.update_idletasks()


if __name__ == "__main__":
    main_window = MainWindow()
    main_window.mainloop()
