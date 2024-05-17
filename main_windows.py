import sys
import tkinter as tk
from tkinter import ttk, StringVar

import serial
import serial.tools.list_ports

from control_frames import SerialControlFrame, TCPControlFrame, MacroControlFrame
from control_services import SerialService, TCPService, MacroService, DisplayService, ConnectionStatusService
from utils.event_dispatcher import EventDispatcher

# TODO: make the display frame work
# TODO: organize macro and individual commands
# TODO: add functionality to status_frame
# TODO: add functionality to display control


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Prealigner Vision Repeatability Test")
        self.log_frame = None
        self.lbl_title = None
        self.ntb_log_control = None
        self.ntb_log = None
        self.ntb_status = None
        self.ntb_control = None
        self.available_ports = []
        self.dispatcher = EventDispatcher()
        self.serial_connection = StringVar()
        self.serial_service = SerialService(dispatcher=self.dispatcher)
        self.tcp_connection = StringVar()
        self.tcp_service = TCPService(dispatcher=self.dispatcher)
        self.macro_service = MacroService()
        self.log_service = DisplayService(dispatcher=self.dispatcher)
        self.display_window = DisplayWindow(self)
        self.flags = {}
        self.initialize_status_flags()
        self.connection_status_service = ConnectionStatusService(self, self.dispatcher)
        self.scan_com_ports()
        self.create_control_frames()
        self.create_connection_status_window()
        self.create_display_window()
        self.register_events()

    def initialize_status_flags(self):
        self.flags = {
            'serial_connection': False,
            'tcp_connection': False,
            'status_3': False,
            'status_4': False,
            'system_busy': False
        }

    def register_events(self):
        self.dispatcher.register_event('connectSerialPort', self.serial_service.connect_serial_port)
        self.dispatcher.register_event('closeSerialPort', self.serial_service.close_serial_port)
        self.dispatcher.register_event('moveToReadyStation', self.serial_service.move_to_ready_station)
        self.dispatcher.register_event('alignWafer', self.serial_service.align_wafer)
        self.dispatcher.register_event('toggleChuck', self.serial_service.toggle_chuck)
        self.dispatcher.register_event('hardwareReset', self.serial_service.hardware_reset)
        self.dispatcher.register_event('sendCustomSerial', self.serial_service.custom_serial_command)

        self.dispatcher.register_event('triggerOne', self.tcp_service.trigger_one)
        self.dispatcher.register_event('triggerTwo', self.tcp_service.trigger_two)
        self.dispatcher.register_event('prevCamera', self.tcp_service.prev_camera)
        self.dispatcher.register_event('nextCamera', self.tcp_service.next_camera)
        self.dispatcher.register_event('sendCustomTCP', self.tcp_service.send_custom_tcp)
        self.dispatcher.register_event('connectTCP', self.tcp_service.connect_tcp_socket)
        self.dispatcher.register_event('disconnectTCP', self.tcp_service.close_tcp_socket)

        self.dispatcher.register_event('stopSequence', self.macro_service.stop_sequence)
        self.dispatcher.register_event('startSequence', self.macro_service.start_sequence)
        self.dispatcher.register_event('stepSequence', self.macro_service.step_sequence)
        self.dispatcher.register_event('resetSequence', self.macro_service.reset_sequence)
        self.dispatcher.register_event('pauseSequence', self.macro_service.pause_sequence)
        self.dispatcher.register_event('continueSequence', self.macro_service.run_sequence)

        self.dispatcher.register_event('getTimestamp', self.log_service.get_timestamp)
        self.dispatcher.register_event('logData', self.log_service.log_data)
        self.dispatcher.register_event('exportLog', self.log_service.export_log)
        self.dispatcher.register_event('displaySent', self.log_service.display_sent)
        self.dispatcher.register_event('displayReceived', self.log_service.display_received)
        self.dispatcher.register_event('displayTimestamp', self.log_service.display_timestamp)
        self.dispatcher.register_event('displayTCPCommunication', self.log_service.display_tcp_communication)
        self.dispatcher.register_event('displaySerialCommunication', self.log_service.display_serial_communication)
        self.dispatcher.register_event('displayAutoScroll', self.log_service.display_auto_scroll)
        self.dispatcher.register_event('updateDisplayWindow', self.display_window.update_display_window)

        self.dispatcher.register_event('updateStatus', self.connection_status_service.check_status)
        self.dispatcher.register_event('serialConnectionTrue', self.connection_status_service.set_serial_connection_true)
        self.dispatcher.register_event('serialConnectionFalse', self.connection_status_service.set_serial_connection_false)
        self.dispatcher.register_event('tcpConnectionTrue', self.connection_status_service.set_tcp_connection_true)
        self.dispatcher.register_event('tcpConnectionFalse', self.connection_status_service.set_tcp_connection_false)
        self.dispatcher.register_event('updateConnectionStatusLabel', self.connection_status_service.update_connection_status_label)

        self.dispatcher.register_event('scanForSerialPorts', self.scan_com_ports)
        self.dispatcher.register_event('quitApplication', self.quit_application)
        self.dispatcher.register_event('emergencyStop', self.emergency_stop)

    def scan_com_ports(self):
        print("Scanning Ports")
        ports = [port.device for port in serial.tools.list_ports.comports()]
        print(f"{ports}")
        self.available_ports = ports
        return ports

    def create_control_frames(self):
        self.ntb_control = ttk.Notebook(self)
        self.ntb_control.grid(row=0, column=0, sticky="n", padx=10, pady=5)

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

    def create_display_window(self):
        self.ntb_log = ttk.Notebook(self)
        self.ntb_log.grid(row=0, rowspan=3, column=1, sticky="", padx=5, pady=5)

        log_tab = ttk.Frame(self.ntb_log)
        self.log_frame = DisplayWindow(log_tab)
        self.log_frame.pack(fill=tk.BOTH, expand=True)
        self.ntb_log.add(log_tab, text="Log")

    def create_connection_status_window(self):
        self.ntb_status = ttk.Notebook(self)
        self.ntb_status.grid(row=1, column=0, sticky='', padx=10, pady=0)

        sts_connection_tab = ttk.Frame(self.ntb_status)
        sts_connection = ConnectionStatusWindow(sts_connection_tab, dispatcher=self.dispatcher)
        sts_connection.pack(fill=tk.BOTH, expand=True)
        self.ntb_status.add(sts_connection_tab, text="Status")

    @staticmethod
    def quit_application():
        print("Quitting")
        sys.exit()

    @staticmethod
    def emergency_stop():
        print("Emergency Stop!")


class DisplayWindow(ttk.Frame):
    def __init__(self, master=None, dispatcher=None):
        super().__init__(master)

        self.dispatcher = dispatcher
        self.log_data = None

        self.display_window = tk.Text(self, width=60)
        self.display_window.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)
        self.display_window.insert(tk.END, "Logging one day soon")

    def update_display_window(self, data_to_log):
        self.display_window.insert(tk.END, data_to_log)
        self.display_window.see(tk.END)
        self.update_idletasks()
        print(f"updating log with: {data_to_log}")


class ConnectionStatusWindow(ttk.Frame):
    def __init__(self, master=None, dispatcher=None):
        super().__init__(master)

        self.dispatcher = dispatcher

        self.serial_connection = tk.StringVar()
        self.serial_connection.set('Not Connected')
        self.lbl_serial_connection = ttk.Label(self, textvariable=self.serial_connection)
        self.lbl_serial_connection.grid(row=0, column=0, sticky="", padx=10)

        self.tcp_connection = tk.StringVar()
        self.tcp_connection.set('Not Connected')
        self.lbl_tcp_connection = ttk.Label(self, textvariable=self.tcp_connection)
        self.lbl_tcp_connection.grid(row=1, column=0, sticky="", padx=10)

        self.lbl_status_3 = ttk.Label(self, text="status 3", state='disabled')
        self.lbl_status_3.grid(row=2, column=0, sticky="", padx=10)

        self.lbl_status_4 = ttk.Label(self, text="status 4", state='disabled')
        self.lbl_status_4.grid(row=3, column=0, sticky="", padx=10)

        self.lbl_system_busy = ttk.Label(self, text="system busy", state='disabled')
        self.lbl_system_busy.grid(row=4, column=0, sticky="", padx=10)



if __name__ == "__main__":
    main_window = MainWindow()
    main_window.mainloop()
