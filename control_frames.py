import tkinter as tk
from tkinter import ttk

# TODO: change Quit to Pause


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

        self.btn_mtrs = ttk.Button(self, text="MTRS", command=lambda: dispatcher.emit('moveToReadyStation'))
        self.btn_mtrs.grid(row=4, column=0, padx=5, pady=(5, 0))

        self.btn_maln = ttk.Button(self, text="MALN", command=lambda: dispatcher.emit('alignWafer'))
        self.btn_maln.grid(row=4, column=1, padx=5, pady=(5, 0))

        self.btn_csol = ttk.Button(self, text="CSOL", command=lambda: dispatcher.emit('toggleChuck'))
        self.btn_csol.grid(row=5, column=0, padx=5)

        self.btn_hrst = ttk.Button(self, text="HRST", command=lambda: dispatcher.emit('hardwareReset'))
        self.btn_hrst.grid(row=5, column=1, padx=5)

        self.ent_custom_serial = ttk.Entry(self)
        self.ent_custom_serial.grid(row=6, column=0, columnspan=2, padx=5, sticky='ew', pady=(5, 0))

        self.btn_custom_serial_send = ttk.Button(self, text="Send", command=lambda: dispatcher.emit('sendCustomSerial', self.ent_custom_serial.get()))
        self.btn_custom_serial_send.grid(row=7, column=0, padx=5)

        self.btn_quit_application = ttk.Button(self, text="Quit", command=lambda: dispatcher.emit('quitApplication'))
        self.btn_quit_application.grid(row=7, column=1, padx=5)

        self.btn_e_stop = ttk.Button(self, text="EMERGENCY STOP", command=lambda: dispatcher.emit('emergencyStop'))
        self.btn_e_stop.grid(row=9, column=0, columnspan=2, padx=5, sticky='ew', pady=(5, 0))


class TCPControlFrame(ttk.Frame):
    def __init__(self, master=None, dispatcher=None):
        super().__init__(master)

        self.dispatcher = dispatcher

        self.lbl_ip_address = ttk.Label(self, text="IP Address")
        self.lbl_ip_address.grid(row=0, column=0, padx=5, pady=5)

        self.txt_ip_address_default = tk.StringVar(value="192.168.1.1")
        self.ent_ip_address = ttk.Entry(self, width=11, textvariable=self.txt_ip_address_default, justify='center')
        self.ent_ip_address.grid(row=1, column=0, padx=5)

        self.lbl_ip_port = ttk.Label(self, text="IP Port")
        self.lbl_ip_port.grid(row=0, column=1, padx=5, pady=5)

        self.txt_ip_port_default = tk.StringVar(value="80")
        self.ent_ip_port = ttk.Entry(self, width=5, textvariable=self.txt_ip_port_default, justify='center')
        self.ent_ip_port.grid(row=1, column=1, padx=5)

        self.btn_connect_socket = ttk.Button(self, text="Connect", command=lambda: dispatcher.emit('connectTCP', self.ent_ip_address.get(), self.ent_ip_port.get()))
        self.btn_connect_socket.grid(row=2, column=0, padx=5)

        self.btn_disconnect_socket = ttk.Button(self, text="Close", command=lambda: dispatcher.emit('disconnectTCP', self.ent_ip_address.get(), self.ent_ip_port.get()))
        self.btn_disconnect_socket.grid(row=2, column=1, padx=5)

        self.btn_t1 = ttk.Button(self, text="Trig 1", command=lambda: dispatcher.emit('triggerOne'))
        self.btn_t1.grid(row=4, column=0, padx=5, pady=(5, 0))

        self.btn_t2 = ttk.Button(self, text="Trig 2", command=lambda: dispatcher.emit('triggerTwo'))
        self.btn_t2.grid(row=4, column=1, padx=5, pady=(5, 0))

        self.btn_prev_camera = ttk.Button(self, text="PrevCam", command=lambda: dispatcher.emit('prevCamera'))
        self.btn_prev_camera.grid(row=5, column=0, padx=5)

        self.btn_next_camera = ttk.Button(self, text="NextCam", command=lambda: dispatcher.emit('nextCamera'))
        self.btn_next_camera.grid(row=5, column=1, padx=5)

        self.ent_custom_tcp = ttk.Entry(self)
        self.ent_custom_tcp.grid(row=6, column=0, columnspan=2, padx=5, sticky='ew', pady=(5, 0))

        self.btn_custom_tcp_send = ttk.Button(self, text="Send", command=lambda: dispatcher.emit('sendCustomTCP', self.ent_custom_tcp.get()))
        self.btn_custom_tcp_send.grid(row=7, column=0, padx=5)

        self.btn_quit_application = ttk.Button(self, text="Quit", command=lambda: dispatcher.emit('quitApplication'))
        self.btn_quit_application.grid(row=7, column=1, padx=5)

        self.btn_e_stop = ttk.Button(self, text="EMERGENCY STOP", command=lambda: dispatcher.emit('emergencyStop'))
        self.btn_e_stop.grid(row=9, column=0, columnspan=2, padx=5, sticky='ew', pady=5)


class MacroControlFrame(ttk.Frame):
    def __init__(self, master=None, dispatcher=None):
        super().__init__(master)

        self.dispatcher = dispatcher

        self.lbl_total_cycles = ttk.Label(self, text="Total Cycles")
        self.lbl_total_cycles.grid(row=0, column=0, padx=5, pady=5)

        self.txt_total_cycles_default = tk.StringVar(value="105")
        self.ent_total_cycles = ttk.Entry(self, width=5, textvariable=self.txt_total_cycles_default, justify='center')
        self.ent_total_cycles.grid(row=1, column=0, padx=5)

        self.lbl_completed_cycles = ttk.Label(self, text="Completed")
        self.lbl_completed_cycles.grid(row=0, column=1, padx=5, pady=5)

        self.lbl_completed_cycles_value = ttk.Label(self, text="0", justify='center')
        self.lbl_completed_cycles_value.grid(row=1, column=1, padx=5)

        self.macro_separator0 = ttk.Separator(self, orient='horizontal')
        self.macro_separator0.grid(row=2, column=0, columnspan=2, sticky='ew', pady=5, padx=5)

        self.btn_start = ttk.Button(self, text="Start", command=lambda: dispatcher.emit('startSequence'))
        self.btn_start.grid(row=3, column=0, padx=5)

        self.btn_stop = ttk.Button(self, text="Stop", command=lambda: dispatcher.emit('stopSequence'))
        self.btn_stop.grid(row=3, column=1, padx=5)

        self.btn_step = ttk.Button(self, text="Step", state='normal', command=lambda: dispatcher.emit('stepSequence'))
        self.btn_step.grid(row=4, column=0, padx=5)

        self.btn_reset = ttk.Button(self, text="Reset", state='normal', command=lambda: dispatcher.emit('resetSequence'))
        self.btn_reset.grid(row=4, column=1, padx=5)

        self.macro_separator1 = ttk.Separator(self, orient='horizontal')
        self.macro_separator1.grid(row=5, column=0, columnspan=2, sticky='ew', pady=5, padx=5)

        self.lbl_start_time = ttk.Label(self, text="Start:")
        self.lbl_start_time.grid(row=6, column=0, padx=5)

        self.val_start_time = ttk.Label(self, text="00:00:00")
        self.val_start_time.grid(row=6, column=1, padx=5)

        self.lbl_stop_time = ttk.Label(self, text="Stop:")
        self.lbl_stop_time.grid(row=7, column=0, pady=5, padx=5)

        self.val_stop_time = ttk.Label(self, text="--:--:--")
        self.val_stop_time.grid(row=7, column=1, pady=5, padx=5)

        self.macro_separator2 = ttk.Separator(self, orient='horizontal')
        self.macro_separator2.grid(row=8, column=0, columnspan=2, sticky='ew', pady=5, padx=5)

        self.btn_e_stop = ttk.Button(self, text="EMERGENCY STOP", command=lambda: dispatcher.emit('emergencyStop'))
        self.btn_e_stop.grid(row=9, column=0, columnspan=2, padx=5, sticky='ew')


class ConnectionStatusFrame(ttk.Frame):
    def __init__(self, master=None, dispatcher=None):
        super().__init__(master)

        self.dispatcher = dispatcher

        self.lbl_serial_connection = ttk.Label(self, text="serial connection", state='disabled')
        self.lbl_serial_connection.grid(row=0, column=0, sticky="", padx=10)

        self.lbl_tcp_connection = ttk.Label(self, text="tcp connection", state='disabled')
        self.lbl_tcp_connection.grid(row=1, column=0, sticky="", padx=10)

        self.lbl_status_3 = ttk.Label(self, text="status 3", state='disabled')
        self.lbl_status_3.grid(row=2, column=0, sticky="", padx=10)

        self.lbl_status_4 = ttk.Label(self, text="status 4", state='disabled')
        self.lbl_status_4.grid(row=3, column=0, sticky="", padx=10)

        self.lbl_system_busy = ttk.Label(self, text="  system busy", state='disabled')
        self.lbl_system_busy.grid(row=4, column=0, sticky="", padx=10)


class DisplayControlFrame(ttk.Frame):
    def __init__(self, master=None, dispatcher=None):
        super().__init__(master)

        self.btn_continue_macro = ttk.Button(self, text="Continue", state='enabled', command=lambda: dispatcher.emit('continueSequence'))
        self.btn_continue_macro.grid(row=1, column=0, sticky='', padx=5)

        self.btn_pause_macro = ttk.Button(self, text="Pause", state='enabled', command=lambda: dispatcher.emit('pauseSequence'))
        self.btn_pause_macro.grid(row=2, column=0, sticky='', padx=5)

        self.btn_macro_log_export = ttk.Button(self, text="Export", state='enabled', command=lambda: dispatcher.emit('exportLog'))
        self.btn_macro_log_export.grid(row=3, column=0, sticky='', padx=5)

        self.macro_separator1 = ttk.Separator(self, orient='vertical')
        self.macro_separator1.grid(row=1, column=1, rowspan=3, sticky='ns', pady=5, padx=5)

        self.var_sent = tk.BooleanVar(value=True)
        self.chk_sent = ttk.Checkbutton(self, text="Sent", variable=self.var_sent, state='normal', command=lambda: dispatcher.emit('displaySent'))
        self.chk_sent.grid(row=1, column=2, sticky='w', padx=5)

        self.var_received = tk.BooleanVar(value=True)
        self.chk_received = ttk.Checkbutton(self, text="Received", variable=self.var_received, state='normal', command=lambda: dispatcher.emit('displayReceived'))
        self.chk_received.grid(row=2, column=2, sticky='w', padx=5)

        self.var_timestamp = tk.BooleanVar(value=True)
        self.chk_timestamp = ttk.Checkbutton(self, text="Timestamp", variable=self.var_timestamp, state='normal', command=lambda: dispatcher.emit('displayTimestamp'))
        self.chk_timestamp.grid(row=3, column=2, sticky='w', padx=5)

        self.macro_separator2 = ttk.Separator(self, orient='vertical')
        self.macro_separator2.grid(row=1, column=3, rowspan=3, sticky='ns', pady=5, padx=5)

        self.var_tcp = tk.BooleanVar(value=True)
        self.chk_tcp = ttk.Checkbutton(self, text="TCP Comm", variable=self.var_tcp, state='normal', command=lambda: dispatcher.emit('displayTCPCommunication'))
        self.chk_tcp.grid(row=1, column=4, sticky='w', padx=5)

        self.var_serial = tk.BooleanVar(value=True)
        self.chk_serial = ttk.Checkbutton(self, text="Serial Comm", variable=self.var_serial, state='normal', command=lambda: dispatcher.emit('displaySerialCommunication'))
        self.chk_serial.grid(row=2, column=4, sticky='w', padx=5)

        self.var_auto_scroll = tk.BooleanVar(value=True)
        self.chk_auto_scroll = ttk.Checkbutton(self, text="Auto-Scroll", variable=self.var_auto_scroll, state='normal', command=lambda: dispatcher.emit('displayAutoScroll'))
        self.chk_auto_scroll.grid(row=3, column=4, sticky='w', padx=5)