# control_frame.py

import tkinter as tk
from datetime import datetime
from tkinter import ttk


class SerialControlFrame(ttk.Frame):
    def __init__(self, master=None, available_ports=None, dispatcher=None):
        super().__init__(master)

        self.dispatcher = dispatcher
        self.serial_connected = False

        self.lbl_com_port = ttk.Label(self, text="COM Port")
        self.lbl_com_port.grid(row=0, column=0, padx=5, pady=(5, 0))

        self.cbx_com_port = ttk.Combobox(self, width=7, values=available_ports)
        self.cbx_com_port.grid(row=1, column=0, pady=0, padx=5)

        self.lbl_baudrate = ttk.Label(self, text="Baud Rate")
        self.lbl_baudrate.grid(row=0, column=1, padx=5, pady=(5, 0))

        self.lbl_9600 = ttk.Label(self, text="9600")
        self.lbl_9600.grid(row=1, column=1, padx=5, pady=5)

        self.btn_connect_serial = ttk.Button(self, text="Connect", command=lambda: dispatcher.emit('connectSerialPort', self.cbx_com_port.get()))
        self.btn_connect_serial.grid(row=2, column=0, padx=5)

        self.btn_disconnect_serial = ttk.Button(self, text="Close", command=lambda: dispatcher.emit('closeSerialPort', self.cbx_com_port.get()))
        self.btn_disconnect_serial.grid(row=2, column=1, padx=5)

        self.serial_separator0 = ttk.Separator(self, orient='horizontal')
        self.serial_separator0.grid(row=3, column=0, columnspan=2, sticky='ew', pady=5, padx=5)

        self.btn_mtrs = ttk.Button(self, text="MTRS", state='disabled', command=lambda: dispatcher.emit('moveToReadyStation'))
        self.btn_mtrs.grid(row=4, column=0, padx=5, pady=0)

        self.btn_maln = ttk.Button(self, text="MALN", state='disabled', command=lambda: dispatcher.emit('alignWafer'))
        self.btn_maln.grid(row=4, column=1, padx=5, pady=0)

        self.btn_chuck_on = ttk.Button(self, text="ChkON", state='disabled', command=lambda: dispatcher.emit('chuckHold'))
        self.btn_chuck_on.grid(row=5, column=0, padx=5)

        self.btn_chuck_off = ttk.Button(self, text="ChkOFF", state='disabled', command=lambda: dispatcher.emit('chuckRelease'))
        self.btn_chuck_off.grid(row=5, column=1, padx=5)

        # self.btn_hrst = ttk.Button(self, text="HRST", state='disabled', command=lambda: dispatcher.emit('hardwareReset'))
        # self.btn_hrst.grid(row=5, column=1, padx=5)

        self.serial_separator1 = ttk.Separator(self, orient='horizontal')
        self.serial_separator1.grid(row=6, column=0, columnspan=2, sticky='ew', pady=5, padx=5)

        self.ent_custom_serial = ttk.Entry(self, state='disabled')
        self.ent_custom_serial.grid(row=7, column=0, columnspan=2, padx=5, sticky='ew', pady=(0, 3))

        self.btn_custom_serial_send = ttk.Button(self, text="Send", state='disabled', command=lambda: dispatcher.emit('sendCustomSerial', self.ent_custom_serial.get()))
        self.btn_custom_serial_send.grid(row=8, column=0, padx=5)

        self.btn_quit_application = ttk.Button(self, text="Quit", command=lambda: dispatcher.emit('quitApplication'))
        self.btn_quit_application.grid(row=8, column=1, padx=5)

        self.serial_separator2 = ttk.Separator(self, orient='horizontal')
        self.serial_separator2.grid(row=9, column=0, columnspan=2, sticky='ew', pady=5, padx=5)

        self.btn_e_stop = ttk.Button(self, text="EMERGENCY STOP", command=lambda: dispatcher.emit('emergencyStop'))
        self.btn_e_stop.grid(row=10, column=0, columnspan=2, padx=5, sticky='ew', pady=(0, 3))

        self.dispatcher.register_event('updateSerialConnectionStatus', self.update_serial_connection_status)

    # UI UPDATES
    def update_serial_connection_status(self, status):
        print("debug this function from SeriaControlFrame0")
        self.serial_connected = status
        self.update_button_states()

    @staticmethod
    def set_widget_states(widgets, state):
        for widget in widgets:
            widget.config(state=state)

    def update_button_states(self):
        print("debug this function from SerialControlFrame")
        widgets = [
            self.btn_mtrs,
            self.btn_maln,
            self.btn_chuck_on,
            self.btn_chuck_off,
            self.btn_custom_serial_send,
            self.ent_custom_serial
        ]

        if self.serial_connected:
            self.set_widget_states(widgets, 'normal')
            self.btn_connect_serial.config(state='disabled')
        else:
            self.set_widget_states(widgets, 'disabled')
            self.btn_connect_serial.config(state='normal')


class TCPControlFrame(ttk.Frame):
    def __init__(self, master=None, dispatcher=None):
        super().__init__(master)

        self.dispatcher = dispatcher
        self.tcp_connected = False

        self.lbl_ip_address = ttk.Label(self, text="IP Address")
        self.lbl_ip_address.grid(row=0, column=0, padx=5, pady=(5, 0))

        self.lbl_ip_port = ttk.Label(self, text="IP Port")
        self.lbl_ip_port.grid(row=0, column=1, padx=0, pady=(5, 0))

        self.txt_ip_address_default = tk.StringVar(value="127.0.0.1")
        self.ent_ip_address = ttk.Entry(self, width=11, textvariable=self.txt_ip_address_default, justify='center')
        self.ent_ip_address.grid(row=1, column=0, padx=5, pady=(5, 3))

        self.txt_ip_port_default = tk.StringVar(value="8500")
        self.ent_ip_port = ttk.Entry(self, width=5, textvariable=self.txt_ip_port_default, justify='center')
        self.ent_ip_port.grid(row=1, column=1, padx=5, pady=(5, 3))

        self.btn_connect_socket = ttk.Button(self, text="Connect", command=lambda: dispatcher.emit('connectTCP', self.ent_ip_address.get(), self.ent_ip_port.get()))
        self.btn_connect_socket.grid(row=2, column=0, padx=5)

        self.btn_disconnect_socket = ttk.Button(self, text="Close", command=lambda: dispatcher.emit('disconnectTCP'))
        self.btn_disconnect_socket.grid(row=2, column=1, padx=5)

        self.tcp_separator0 = ttk.Separator(self, orient='horizontal')
        self.tcp_separator0.grid(row=3, column=0, columnspan=2, sticky='ew', pady=5, padx=5)

        self.btn_t1 = ttk.Button(self, text="Trig 1", state='disabled', command=lambda: dispatcher.emit('triggerOne'))
        self.btn_t1.grid(row=4, column=0, padx=5, pady=0)

        self.btn_t2 = ttk.Button(self, text="Trig 2", state='disabled', command=lambda: dispatcher.emit('triggerTwo'))
        self.btn_t2.grid(row=4, column=1, padx=5, pady=0)

        self.btn_prev_camera = ttk.Button(self, text="PrevCam", state='disabled', command=lambda: dispatcher.emit('prevCamera'))
        self.btn_prev_camera.grid(row=5, column=0, padx=5)

        self.btn_next_camera = ttk.Button(self, text="NextCam", state='disabled', command=lambda: dispatcher.emit('nextCamera'))
        self.btn_next_camera.grid(row=5, column=1, padx=5)

        self.tcp_separator1 = ttk.Separator(self, orient='horizontal')
        self.tcp_separator1.grid(row=6, column=0, columnspan=2, sticky='ew', pady=5, padx=5)

        self.ent_custom_tcp = ttk.Entry(self, state='disabled')
        self.ent_custom_tcp.grid(row=7, column=0, columnspan=2, padx=5, sticky='ew', pady=(0, 3))

        self.btn_custom_tcp_send = ttk.Button(self, text="Send", state='disabled', command=lambda: dispatcher.emit('sendCustomTCP', self.ent_custom_tcp.get()))
        self.btn_custom_tcp_send.grid(row=8, column=0, padx=5)

        self.btn_quit_application = ttk.Button(self, text="Quit", command=lambda: dispatcher.emit('quitApplication'))
        self.btn_quit_application.grid(row=8, column=1, padx=5)

        self.tcp_separator2 = ttk.Separator(self, orient='horizontal')
        self.tcp_separator2.grid(row=9, column=0, columnspan=2, sticky='ew', pady=5, padx=5)

        self.btn_e_stop = ttk.Button(self, text="EMERGENCY STOP", command=lambda: dispatcher.emit('emergencyStop'))
        self.btn_e_stop.grid(row=10, column=0, columnspan=2, padx=5, sticky='ew', pady=(0, 3))

        self.dispatcher.register_event('updateTCPConnectionStatus', self.update_tcp_connection_status)

        # UI UPDATES
    def update_tcp_connection_status(self, status):
        print("debug this function from TCPControlFrame0")
        self.tcp_connected = status
        self.update_button_states()

    @staticmethod
    def set_widget_states(widgets, state):
        for widget in widgets:
            widget.config(state=state)

    def update_button_states(self):
        print("debug this function from TCPControlFrame1")
        widgets = [
            self.btn_t1,
            self.btn_t2,
            self.btn_prev_camera,
            self.btn_next_camera,
            self.btn_custom_tcp_send,
            self.ent_custom_tcp
        ]

        if self.tcp_connected:
            self.set_widget_states(widgets, 'normal')
            self.btn_connect_socket.config(state='disabled')
        else:
            self.set_widget_states(widgets, 'disabled')
            self.btn_connect_socket.config(state='normal')


class MacroControlFrame(ttk.Frame):
    def __init__(self, master=None, dispatcher=None, completed_cycles_value=None):
        super().__init__(master)
        self.total_cycles = tk.StringVar(value="105")

        self.stop_time = None
        self.dispatcher = dispatcher
        self.completed_cycles_value = completed_cycles_value or tk.IntVar(value=0)
        self.start_time = None
        self.elapsed_time = tk.StringVar(value="00:00:00")
        self.macro_running = False

        self.serial_connected = False
        self.tcp_connected = True

        self.lbl_alignments = ttk.Label(self, text="Alignments")
        self.lbl_alignments.grid(row=1, column=0, padx=5, pady=5)

        self.ent_total_cycles = ttk.Entry(self, width=5, textvariable=self.total_cycles, justify='center')
        self.ent_total_cycles.grid(row=2, column=0, padx=5)
        self.ent_total_cycles.bind("<FocusOut>", lambda event: self.on_total_cycles_change())
        self.ent_total_cycles.bind("<Return>", lambda event: self.on_total_cycles_change())

        self.lbl_completed_cycles = ttk.Label(self, text="Completed")
        self.lbl_completed_cycles.grid(row=1, column=1, padx=5, pady=5)

        self.ent_completed_cycles = ttk.Entry(self, width=5, justify='center', textvariable=self.completed_cycles_value)
        self.ent_completed_cycles.grid(row=2, column=1, padx=5)

        self.macro_separator0 = ttk.Separator(self, orient='horizontal')
        self.macro_separator0.grid(row=3, column=0, columnspan=2, sticky='ew', pady=5, padx=5)

        self.btn_start = ttk.Button(self, text="Start", state='disabled', command=self.starting_sequence)
        self.btn_start.grid(row=4, column=0, padx=5)

        self.btn_stop = ttk.Button(self, text="Stop", state='normal', command=lambda: dispatcher.emit('stopSequence'))
        self.btn_stop.grid(row=4, column=1, padx=5)

        self.btn_clear_log_display = ttk.Button(self, text="Clear", state='normal', command=lambda: dispatcher.emit('clearLogDisplay'))
        self.btn_clear_log_display.grid(row=5, column=0, padx=5)

        self.btn_reset = ttk.Button(self, text="Reset", state='disabled', command=self.reset_sequence)
        self.btn_reset.grid(row=5, column=1, padx=5)

        self.macro_separator1 = ttk.Separator(self, orient='horizontal')
        self.macro_separator1.grid(row=6, column=0, columnspan=2, sticky='ew', pady=(5, 8), padx=5)

        self.lbl_start_time = ttk.Label(self, text="Started:")
        self.lbl_start_time.grid(row=7, column=0, padx=5)

        self.val_start_time = ttk.Label(self, text="00:00:00")
        self.val_start_time.grid(row=7, column=1, padx=5)

        self.lbl_elapsed_time = ttk.Label(self, text="Elapsed:")
        self.lbl_elapsed_time.grid(row=8, column=0, pady=5, padx=5)

        self.val_elapsed_time = ttk.Label(self, text="--:--:--")
        self.val_elapsed_time.grid(row=8, column=1, pady=5, padx=5)

        self.lbl_stop_time = ttk.Label(self, text="Stopped:")
        self.lbl_stop_time.grid(row=9, column=0, pady=(0, 4), padx=5)

        self.val_stop_time = ttk.Label(self, text="--:--:--")
        self.val_stop_time.grid(row=9, column=1, pady=(0, 4), padx=5)

        self.macro_separator2 = ttk.Separator(self, orient='horizontal')
        self.macro_separator2.grid(row=10, column=0, columnspan=2, sticky='ew', pady=(8, 5), padx=5)

        self.btn_e_stop = ttk.Button(self, text="EMERGENCY STOP", command=lambda: dispatcher.emit('emergencyStop'))
        self.btn_e_stop.grid(row=11, column=0, columnspan=2, padx=5, pady=0, sticky='ew')

        self.dispatcher.register_event('updateSerialConnectionStatus', self.update_serial_connection_status)
        self.dispatcher.register_event('updateTCPConnectionStatus', self.update_tcp_connection_status)
        self.dispatcher.register_event('startSequence', self.set_start_time)
        self.dispatcher.register_event('stopSequence', self.set_stop_time)

        self.update_button_states()

    def on_total_cycles_change(self):
        new_total = self.total_cycles.get()
        self.dispatcher.emit('updateTotalCycles', new_total)
        self.dispatcher.emit('total_cycles_update', new_total)

    def starting_sequence(self):
        self.set_start_time()
        self.dispatcher.emit('initializeSequence', self.ent_total_cycles.get())
        self.macro_running = True
        self.update_elapsed_time()
        self.update_button_states()

    def update_serial_connection_status(self, status):
        print("debug this function from MacroControlFrame0")
        self.serial_connected = status
        self.update_button_states()

    def update_tcp_connection_status(self, status):
        print("debug this function from MacroControlFrame1")
        self.tcp_connected = status
        self.update_button_states()

    def update_button_states(self):
        if self.serial_connected:
            self.btn_start.config(state='normal')
        else:
            self.btn_start.config(state='disabled')

        if self.macro_running:
            self.btn_reset.config(state='disabled')
            self.btn_start.config(state='disabled')
        else:
            self.btn_reset.config(state='normal')
            self.btn_start.config(state='normal')

    def set_start_time(self):
        print("debug this function from MacroControlFrame2")
        self.start_time = datetime.now()
        self.val_start_time.config(text=self.start_time.strftime("%H:%M:%S"))
        print(f"Start time set to: {self.start_time.strftime('%H:%M:%S')}")

    def set_stop_time(self):
        print("debug this function from MacroControlFrame3")
        self.stop_time = datetime.now()
        self.val_stop_time.config(text=self.stop_time.strftime("%H:%M:%S"))
        print(f"Stop time set to: {self.stop_time.strftime('%H:%M:%S')}")
        self.macro_running = False
        self.update_elapsed_time()
        self.update_button_states()

    def update_elapsed_time(self):
        if self.start_time and self.macro_running:
            elapsed = datetime.now() - self.start_time
            self.elapsed_time.set(str(elapsed).split('.')[0])  # Format as HH:MM:SS
            self.val_elapsed_time.config(text=self.elapsed_time.get())
            self.after(1000, self.update_elapsed_time)  # Schedule to update every second
        elif self.start_time and self.stop_time:
            elapsed = self.stop_time - self.start_time
            self.elapsed_time.set(str(elapsed).split('.')[0])  # Format as HH:MM:SS
            self.val_elapsed_time.config(text=self.elapsed_time.get())
        else:
            self.val_elapsed_time.config(text="--:--:--")

    def reset_sequence(self):
        print("debug this function from MacroControlFrame5")
        print("Sequence Reset")
        self.macro_running = False
        self.start_time = None
        self.stop_time = None
        self.val_start_time.config(text="00:00:00")
        self.val_stop_time.config(text="--:--:--")
        self.val_elapsed_time.config(text="--:--:--")
        self.elapsed_time.set("00:00:00")
        self.ent_total_cycles.delete(0, tk.END)
        self.ent_total_cycles.insert(0, "105")
        self.ent_completed_cycles.delete(0, tk.END)
        self.ent_completed_cycles.insert(0, "0")
        self.update_button_states()


class StatusFrame(tk.Frame):
    def __init__(self, master=None, dispatcher=None):
        super().__init__(master)
        self.dispatcher = dispatcher
        self.status_label_width = 16

        self.lbl_serial_status = tk.Label(self, text="Serial: Disconnected", width=self.status_label_width, foreground="dark grey")
        self.lbl_serial_status.grid(row=0, column=0, padx=0, pady=5, sticky='ew')

        self.lbl_tcp_status = tk.Label(self, text="TCP: Disconnected", width=self.status_label_width, foreground="dark grey")
        self.lbl_tcp_status.grid(row=1, column=0, padx=0, pady=0, sticky='ew')

        self.lbl_macro_status = tk.Label(self, text="Macro: Stopped", width=self.status_label_width, foreground="dark grey")
        self.lbl_macro_status.grid(row=2, column=0, padx=0, pady=5, sticky='ew')
        """TODO: move these out of here"""
        self.dispatcher.register_event('updateSerialConnectionStatus', self.update_serial_status)
        self.dispatcher.register_event('updateTCPConnectionStatus', self.update_tcp_status)
        self.dispatcher.register_event('updateMacroRunningStatus', self.update_macro_status)

    # UI UPDATES
    def update_serial_status(self, status):
        if status:
            self.lbl_serial_status.config(text="SERIAL: Connected", foreground="white", background='green')
        else:
            self.lbl_serial_status.config(text="SERIAL: Closed", foreground="white", background='red')

    def update_tcp_status(self, status):
        if status:
            self.lbl_tcp_status.config(text="TCP: Connected", foreground="white", background='green')
        else:
            self.lbl_tcp_status.config(text="TCP: Closed", foreground="white", background='red')

    def update_macro_status(self, status):
        if status:
            self.lbl_macro_status.config(text="MACRO: Running", foreground="white", background='green')
        else:
            self.lbl_macro_status.config(text="MACRO: Stopped", foreground="white", background='red')
