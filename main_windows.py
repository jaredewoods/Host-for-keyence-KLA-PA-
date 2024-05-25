# main_windows.py
# TODO make the custom serial service work
import sys
import tkinter as tk
from datetime import datetime
from tkinter import ttk, scrolledtext, Menu
import subprocess
import serial
import serial.tools.list_ports

from control_frames import SerialControlFrame, TCPControlFrame, MacroControlFrame, StatusFrame
from control_services import SerialService, TCPService, MacroService
from event_dispatcher import EventDispatcher
from event_dispatcher import register_events


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.completed_cycles = None
        self.total_cycles = None
        self.status_frame = None
        self.log_display = None
        self.serial_connected = False
        self.tcp_connected = False
        self.macro_running = False
        self.completed_cycles_value = tk.IntVar(value=0)
        print("Initializing MainWindow")
        self.title("KLA Prealigner Vision Repeatability (Keyence)")
        self.ntb_control = None
        self.available_ports = []
        self.dispatcher = EventDispatcher()
        self.serial_service = SerialService(dispatcher=self.dispatcher)
        self.tcp_service = TCPService(dispatcher=self.dispatcher)
        self.macro_service = MacroService(dispatcher=self.dispatcher,
                                          serial_service=self.serial_service,
                                          tcp_service=self.tcp_service)
        self.scan_com_ports()
        self.create_control_frames()
        self.create_log_frame()
        self.create_status_frame()
        self.create_menu_bar()
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
        self.ntb_control.add(serial_control_tab, text="   Serial   ")

        tcp_control_tab = ttk.Frame(self.ntb_control)
        tcp_control = TCPControlFrame(tcp_control_tab, dispatcher=self.dispatcher)
        tcp_control.pack(fill=tk.BOTH, expand=True)
        self.ntb_control.add(tcp_control_tab, text="    TCP    ")
        self.ntb_control.bind("<<NotebookTabChanged>>", self.on_tab_change)
        print("Control Frames created.")

        macro_control_tab = ttk.Frame(self.ntb_control)
        macro_control = MacroControlFrame(macro_control_tab, dispatcher=self.dispatcher,
                                          completed_cycles_value=self.completed_cycles_value)
        macro_control.pack(fill=tk.BOTH, expand=True)
        self.ntb_control.add(macro_control_tab, text="   Macro   ")

    def create_log_frame(self):
        self.log_display = scrolledtext.ScrolledText(self, wrap=tk.WORD, height=22, width=62)
        self.log_display.grid(row=0, column=1, rowspan=2, sticky="", padx=5, pady=5)
        fallback_fonts = ("Consolas", "Courier New", "Lucida Console", "monospace")
        self.log_display.configure(bg="#000040", fg="yellow", font=(fallback_fonts, 10))

    def clear_log_display(self):
        self.log_display.delete('1.0', tk.END)
        print("Log Display cleared")

    def create_status_frame(self):
        self.status_frame = StatusFrame(self, dispatcher=self.dispatcher)
        self.status_frame.grid(row=1, column=0, padx=5, pady=5)
        self.status_frame.grid_propagate(False)
        self.status_frame.config(width=150, height=90)

    def log_to_display(self, message, source):
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_message = f"[{timestamp}] {source} {message}"
        self.log_display.insert(tk.END, f"{log_message}\n")
        self.log_display.see(tk.END)

    def update_serial_connection_status(self, status):
        print("debug this function from MainWindow")
        self.serial_connected = status
        self.dispatcher.emit('updateButtonStates')

    def update_tcp_connection_status(self, status):
        print("debug this function from MainWindow")
        self.tcp_connected = status
        self.dispatcher.emit('updateButtonStates')

    def update_macro_running_status(self, status):
        print("debug this function from MainWindow")
        self.macro_running = status
        print(f'macro running status: {status}')

    def update_completed_cycles_display(self, completed_cycles):
        print("debug this function from MainWindow")
        print(f"Updating completed cycles value: {completed_cycles}")
        self.completed_cycles_value.set(completed_cycles)
        print(f"New value in IntVar: {self.completed_cycles_value.get()}")
        self.update_idletasks()

    def on_tab_change(self, event):  # forces immediate update
        self.ntb_control.update_idletasks()

    def create_menu_bar(self):
        # Create a menu bar
        menu_bar = Menu(self)

        # Create the File menu
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Preferences", command=self.show_about)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit_application)
        menu_bar.add_cascade(label="File", menu=file_menu)

        # Create the Edit menu
        settings_menu = Menu(menu_bar, tearoff=0)
        settings_menu.add_command(label="Serial Settings", command=self.show_about)
        settings_menu.add_command(label="TCP Settings", command=self.show_about)

        menu_bar.add_cascade(label="Settings", menu=settings_menu)

        # Create the Windows menu
        windows_menu = Menu(menu_bar, tearoff=0)
        windows_menu.add_command(label="Macro Status", command=self.show_about)

        menu_bar.add_cascade(label="Windows", menu=windows_menu)

        # Create the Windows menu
        simulator_menu = Menu(menu_bar, tearoff=0)
        simulator_menu.add_command(label="Launch NXC100 Simulator", command=self.launch_simulator)

        menu_bar.add_cascade(label="Simulator", menu=simulator_menu)

        # Create the Help menu
        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        menu_bar.add_cascade(label="Help", menu=help_menu)

        # Set the menu bar
        self.config(menu=menu_bar)

    @staticmethod
    def show_about():
        print("You selected an option reserved for future use")

    @staticmethod
    def quit_application():
        print("Quitting")
        sys.exit()

    @staticmethod
    def launch_simulator():
        subprocess.Popen(["python", "NXC100_simulator.py"])


if __name__ == "__main__":
    main_window = MainWindow()
    main_window.mainloop()
