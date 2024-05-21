# control_frame.py

import tkinter as tk
from tkinter import ttk


class SerialControlFrame(ttk.Frame):
    def __init__(self, master=None, available_ports=None, dispatcher=None):
        super().__init__(master)

        self.dispatcher = dispatcher

        self.lbl_com_port = ttk.Label(self, text="COM Port")
        self.lbl_com_port.grid(row=0, column=0, padx=5, pady=5)

        self.cbx_com_port = ttk.Combobox(self, width=7, values=available_ports)
        self.cbx_com_port.grid(row=1, column=0, pady=0, padx=5)

        self.lbl_baudrate = ttk.Label(self, text="baud 9600")
        self.lbl_baudrate.grid(row=0, column=1, padx=5, pady=5)

        self.btn_refresh = ttk.Button(self, text="Refresh", command=lambda: dispatcher.emit('scanForSerialPorts'))
        self.btn_refresh.grid(row=1, column=1, padx=5)

        self.btn_connect_serial = ttk.Button(self, text="Connect", command=lambda: dispatcher.emit('connectSerialPort', self.cbx_com_port.get()))
        self.btn_connect_serial.grid(row=2, column=0, padx=5)

        self.btn_disconnect_serial = ttk.Button(self, text="Close", command=lambda: dispatcher.emit('closeSerialPort', self.cbx_com_port.get()))
        self.btn_disconnect_serial.grid(row=2, column=1, padx=5)

        self.serial_separator0 = ttk.Separator(self, orient='horizontal')
        self.serial_separator0.grid(row=3, column=0, columnspan=2, sticky='ew', pady=5, padx=5)

        self.btn_mtrs = ttk.Button(self, text="MTRS", command=lambda: dispatcher.emit('moveToReadyStation'))
        self.btn_mtrs.grid(row=4, column=0, padx=5, pady=0)

        self.btn_maln = ttk.Button(self, text="MALN", command=lambda: dispatcher.emit('alignWafer'))
        self.btn_maln.grid(row=4, column=1, padx=5, pady=0)

        self.btn_csol = ttk.Button(self, text="@+$", command=lambda: dispatcher.emit('toggleChuck'))
        self.btn_csol.grid(row=5, column=0, padx=5)

        self.btn_hrst = ttk.Button(self, text="@", command=lambda: dispatcher.emit('hardwareReset'))
        self.btn_hrst.grid(row=5, column=1, padx=5)

        self.serial_separator1 = ttk.Separator(self, orient='horizontal')
        self.serial_separator1.grid(row=6, column=0, columnspan=2, sticky='ew', pady=5, padx=5)

        self.ent_custom_serial = ttk.Entry(self)
        self.ent_custom_serial.grid(row=7, column=0, columnspan=2, padx=5, sticky='ew', pady=0)

        self.btn_custom_serial_send = ttk.Button(self, text="Send", command=lambda: dispatcher.emit('sendCustomSerial', self.ent_custom_serial.get()))
        self.btn_custom_serial_send.grid(row=8, column=0, padx=5)

        self.btn_quit_application = ttk.Button(self, text="Quit", command=lambda: dispatcher.emit('quitApplication'))
        self.btn_quit_application.grid(row=8, column=1, padx=5)

        self.serial_separator2 = ttk.Separator(self, orient='horizontal')
        self.serial_separator2.grid(row=9, column=0, columnspan=2, sticky='ew', pady=5, padx=5)

        self.btn_e_stop = ttk.Button(self, text="EMERGENCY STOP", command=lambda: dispatcher.emit('emergencyStop'))
        self.btn_e_stop.grid(row=10, column=0, columnspan=2, padx=5, sticky='ew', pady=0)


class TCPControlFrame(ttk.Frame):
    def __init__(self, master=None, dispatcher=None):
        super().__init__(master)

        self.dispatcher = dispatcher

        self.lbl_ip_address = ttk.Label(self, text="  IP Address")
        self.lbl_ip_address.grid(row=0, column=0, padx=5, pady=5)

        self.lbl_ip_port = ttk.Label(self, text="          IP Port")
        self.lbl_ip_port.grid(row=0, column=1, padx=0, pady=5)

        self.txt_ip_address_default = tk.StringVar(value="192.168.1.1")
        self.ent_ip_address = ttk.Entry(self, width=11, textvariable=self.txt_ip_address_default, justify='center')
        self.ent_ip_address.grid(row=1, column=0, columnspan=2, sticky='w', padx=5)

        self.txt_ip_port_default = tk.StringVar(value="80")
        self.ent_ip_port = ttk.Entry(self, width=5, textvariable=self.txt_ip_port_default, justify='center')
        self.ent_ip_port.grid(row=1, column=1, columnspan=2, sticky='e', padx=5)

        self.btn_connect_socket = ttk.Button(self, text="Connect", command=lambda: dispatcher.emit('connectTCP', self.ent_ip_address.get(), self.ent_ip_port.get()))
        self.btn_connect_socket.grid(row=2, column=0, padx=5)

        self.btn_disconnect_socket = ttk.Button(self, text="Close", command=lambda: dispatcher.emit('disconnectTCP', self.ent_ip_address.get(), self.ent_ip_port.get()))
        self.btn_disconnect_socket.grid(row=2, column=1, padx=5)

        self.tcp_separator0 = ttk.Separator(self, orient='horizontal')
        self.tcp_separator0.grid(row=3, column=0, columnspan=2, sticky='ew', pady=5, padx=5)

        self.btn_t1 = ttk.Button(self, text="Trig 1", command=lambda: dispatcher.emit('triggerOne'))
        self.btn_t1.grid(row=4, column=0, padx=5, pady=0)

        self.btn_t2 = ttk.Button(self, text="Trig 2", command=lambda: dispatcher.emit('triggerTwo'))
        self.btn_t2.grid(row=4, column=1, padx=5, pady=0)

        self.btn_prev_camera = ttk.Button(self, text="PrevCam", command=lambda: dispatcher.emit('prevCamera'))
        self.btn_prev_camera.grid(row=5, column=0, padx=5)

        self.btn_next_camera = ttk.Button(self, text="NextCam", command=lambda: dispatcher.emit('nextCamera'))
        self.btn_next_camera.grid(row=5, column=1, padx=5)

        self.tcp_separator1 = ttk.Separator(self, orient='horizontal')
        self.tcp_separator1.grid(row=6, column=0, columnspan=2, sticky='ew', pady=5, padx=5)

        self.ent_custom_tcp = ttk.Entry(self)
        self.ent_custom_tcp.grid(row=7, column=0, columnspan=2, padx=5, sticky='ew', pady=0)

        self.btn_custom_tcp_send = ttk.Button(self, text="Send", command=lambda: dispatcher.emit('sendCustomTCP', self.ent_custom_tcp.get()))
        self.btn_custom_tcp_send.grid(row=8, column=0, padx=5)

        self.btn_quit_application = ttk.Button(self, text="Quit", command=lambda: dispatcher.emit('quitApplication'))
        self.btn_quit_application.grid(row=8, column=1, padx=5)

        self.tcp_separator1 = ttk.Separator(self, orient='horizontal')
        self.tcp_separator1.grid(row=9, column=0, columnspan=2, sticky='ew', pady=5, padx=5)

        self.btn_e_stop = ttk.Button(self, text="EMERGENCY STOP", command=lambda: dispatcher.emit('emergencyStop'))
        self.btn_e_stop.grid(row=10, column=0, columnspan=2, padx=5, sticky='ew', pady=0)


class MacroControlFrame(ttk.Frame):
    def __init__(self, master=None, dispatcher=None):
        super().__init__(master)

        self.dispatcher = dispatcher
        self.serial_connected = False
        self.tcp_connected = False

        self.lbl_alignments = ttk.Label(self, text="ROUND 1 of 5")
        self.lbl_alignments.grid(row=0, column=0, columnspan=2, sticky="", padx=5, pady=5)

        self.lbl_alignments = ttk.Label(self, text="Alignments")
        self.lbl_alignments.grid(row=1, column=0, padx=5, pady=5)

        self.txt_total_cycles_default = tk.StringVar(value="105")
        self.ent_total_cycles = ttk.Entry(self, width=5, textvariable=self.txt_total_cycles_default, justify='center')
        self.ent_total_cycles.grid(row=2, column=0, padx=5)

        self.lbl_completed_cycles = ttk.Label(self, text="Completed")
        self.lbl_completed_cycles.grid(row=1, column=1, padx=5, pady=5)

        self.lbl_completed_cycles_value = ttk.Label(self, text="0", justify='center')
        self.lbl_completed_cycles_value.grid(row=2, column=1, padx=5)

        self.macro_separator0 = ttk.Separator(self, orient='horizontal')
        self.macro_separator0.grid(row=3, column=0, columnspan=2, sticky='ew', pady=5, padx=5)

        self.btn_start = ttk.Button(self, text="Start", state='disabled', command=lambda: dispatcher.emit('startSequence'))
        self.btn_start.grid(row=4, column=0, padx=5)

        self.btn_stop = ttk.Button(self, text="Stop", state='normal', command=lambda: dispatcher.emit('stopSequence'))
        self.btn_stop.grid(row=4, column=1, padx=5)

        self.btn_step = ttk.Button(self, text="Step", state='disabled', command=lambda: dispatcher.emit('stepSequence'))
        self.btn_step.grid(row=5, column=0, padx=5)

        self.btn_reset = ttk.Button(self, text="Reset", state='normal', command=lambda: dispatcher.emit('resetSequence'))
        self.btn_reset.grid(row=5, column=1, padx=5)

        self.macro_separator1 = ttk.Separator(self, orient='horizontal')
        self.macro_separator1.grid(row=6, column=0, columnspan=2, sticky='ew', pady=(5, 8), padx=5)

        self.lbl_start_time = ttk.Label(self, text="Start:")
        self.lbl_start_time.grid(row=7, column=0, padx=5)

        self.val_start_time = ttk.Label(self, text="00:00:00")
        self.val_start_time.grid(row=7, column=1, padx=5)

        self.lbl_stop_time = ttk.Label(self, text="Stop:")
        self.lbl_stop_time.grid(row=8, column=0, pady=5, padx=5)

        self.val_stop_time = ttk.Label(self, text="--:--:--")
        self.val_stop_time.grid(row=8, column=1, pady=5, padx=5)

        self.macro_separator2 = ttk.Separator(self, orient='horizontal')
        self.macro_separator2.grid(row=9, column=0, columnspan=2, sticky='ew', pady=5, padx=5)

        self.btn_e_stop = ttk.Button(self, text="EMERGENCY STOP", command=lambda: dispatcher.emit('emergencyStop'))
        self.btn_e_stop.grid(row=10, column=0, columnspan=2, padx=5, pady=0, sticky='ew')

        self.dispatcher.register_event('updateSerialConnectionStatus', self.update_serial_connection_status)
        self.dispatcher.register_event('updateTCPConnectionStatus', self.update_tcp_connection_status)

    def update_serial_connection_status(self, status):
        self.serial_connected = status
        self.update_button_states()

    def update_tcp_connection_status(self, status):
        self.tcp_connected = status
        self.update_button_states()

    def update_button_states(self):
        if self.serial_connected and self.tcp_connected:
            self.btn_start.config(state='normal')
            self.btn_step.config(state='normal')
        else:
            self.btn_start.config(state='disabled')
            self.btn_step.config(state='disabled')


class StatusFrame(ttk.Frame):
    def __init__(self, master=None, dispatcher=None):
        super().__init__(master)
        self.dispatcher = dispatcher

        # Create a LabelFrame to hold the status labels
        self.status_label_frame = ttk.LabelFrame(self, text="      Connection Status")
        self.status_label_frame.grid(row=0, column=0, padx=10, pady=(0, 20), sticky="new")

        self.lbl_serial_status = ttk.Label(self.status_label_frame, text="Serial: Disconnected", foreground="dark red")
        self.lbl_serial_status.grid(row=0, column=0, padx=20, pady=(10, 5))

        self.lbl_tcp_status = ttk.Label(self.status_label_frame, text="TCP: Disconnected", foreground="dark red")
        self.lbl_tcp_status.grid(row=1, column=0, padx=20, pady=(0, 5))

        self.lbl_macro_status = ttk.Label(self.status_label_frame, text="Macro: Stopped", foreground="dark red")
        self.lbl_macro_status.grid(row=2, column=0, padx=20, pady=(0, 10))

        self.dispatcher.register_event('updateSerialConnectionStatus', self.update_serial_status)
        self.dispatcher.register_event('updateTCPConnectionStatus', self.update_tcp_status)
        self.dispatcher.register_event('updateMacroRunningStatus', self.update_macro_status)

    def update_serial_status(self, status):
        if status:
            self.lbl_serial_status.config(text="Serial: Connected", foreground="green")
        else:
            self.lbl_serial_status.config(text="Serial: Disconnected", foreground="red")

    def update_tcp_status(self, status):
        if status:
            self.lbl_tcp_status.config(text="TCP: Connected", foreground="green")
        else:
            self.lbl_tcp_status.config(text="TCP: Disconnected", foreground="red")

    def update_macro_status(self, status):
        if status:
            self.lbl_macro_status.config(text="Macro: Running", foreground="green")
        else:
            self.lbl_macro_status.config(text="Macro: Stopped", foreground="red")
