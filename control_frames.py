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

        self.btn_csol = ttk.Button(self, text="CSOL", state='disabled', command=lambda: dispatcher.emit('chuckHold'))
        self.btn_csol.grid(row=5, column=0, padx=5)

        self.btn_hrst = ttk.Button(self, text="HRST", state='disabled', command=lambda: dispatcher.emit('hardwareReset'))
        self.btn_hrst.grid(row=5, column=1, padx=5)

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
        print("debug this function from SeriaControlFrame")
        self.serial_connected = status
        self.update_button_states()

    def update_button_states(self):
        print("debug this function from SeriaControlFrame")
        if self.serial_connected:
            self.btn_mtrs.config(state='normal')
            self.btn_maln.config(state='normal')
            self.btn_csol.config(state='normal')
            self.btn_hrst.config(state='normal')
            self.btn_custom_serial_send.config(state='normal')
            self.ent_custom_serial.config(state='normal')

        else:
            self.btn_mtrs.config(state='disabled')
            self.btn_maln.config(state='disabled')
            self.btn_csol.config(state='disabled')
            self.btn_hrst.config(state='disabled')
            self.btn_custom_serial_send.config(state='disabled')
            self.ent_custom_serial.config(state='disabled')


class TCPControlFrame(ttk.Frame):
    def __init__(self, master=None, dispatcher=None):
        super().__init__(master)

        self.dispatcher = dispatcher
        self.tcp_connected = False

        self.lbl_ip_address = ttk.Label(self, text="IP Address")
        self.lbl_ip_address.grid(row=0, column=0, padx=5, pady=(5, 0))

        self.lbl_ip_port = ttk.Label(self, text="IP Port")
        self.lbl_ip_port.grid(row=0, column=1, padx=0, pady=(5, 0))

        self.txt_ip_address_default = tk.StringVar(value="192.168.1.1")
        self.ent_ip_address = ttk.Entry(self, width=11, textvariable=self.txt_ip_address_default, justify='center')
        self.ent_ip_address.grid(row=1, column=0, padx=5, pady=(5, 3))

        self.txt_ip_port_default = tk.StringVar(value="80")
        self.ent_ip_port = ttk.Entry(self, width=5, textvariable=self.txt_ip_port_default, justify='center')
        self.ent_ip_port.grid(row=1, column=1, padx=5, pady=(5, 3))

        self.btn_connect_socket = ttk.Button(self, text="Connect", command=lambda: dispatcher.emit('connectTCP', self.ent_ip_address.get(), self.ent_ip_port.get()))
        self.btn_connect_socket.grid(row=2, column=0, padx=5)

        self.btn_disconnect_socket = ttk.Button(self, text="Close", command=lambda: dispatcher.emit('disconnectTCP', self.ent_ip_address.get(), self.ent_ip_port.get()))
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
        print("debug this function from TCPControlFrame")
        self.tcp_connected = status
        self.update_button_states()

    def update_button_states(self):
        print("debug this function from TCPControlFrame")
        if self.tcp_connected:
            self.btn_t1.config(state='normal')
            self.btn_t2.config(state='normal')
            self.btn_prev_camera.config(state='normal')
            self.btn_next_camera.config(state='normal')
            self.btn_custom_tcp_send.config(state='normal')
            self.ent_custom_tcp.config(state='normal')
        else:
            self.btn_t1.config(state='disabled')
            self.btn_t2.config(state='disabled')
            self.btn_prev_camera.config(state='disabled')
            self.btn_next_camera.config(state='disabled')
            self.btn_custom_tcp_send.config(state='disabled')
            self.ent_custom_tcp.config(state='disabled')


class MacroControlFrame(ttk.Frame):
    def __init__(self, master=None, dispatcher=None, completed_cycles_value=None, total_cycles=None):
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

        self.btn_clear_log_display = ttk.Button(self, text="Clear", state='enabled', command=lambda: dispatcher.emit('clearLogDisplay'))
        self.btn_clear_log_display.grid(row=5, column=0, padx=5)

        self.btn_reset = ttk.Button(self, text="Reset", state='normal', command=self.reset_sequence)
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

    # UI UPDATES
    def starting_sequence(self):
        self.set_start_time()
        self.dispatcher.emit('initializeSequence', self.ent_total_cycles.get())
        self.macro_running = True  # Set the flag when the sequence starts
        self.update_elapsed_time()  # Start the timer

    def update_serial_connection_status(self, status):
        print("debug this function from MacroControlFrame")
        self.serial_connected = status
        self.update_button_states()

    def update_tcp_connection_status(self, status):
        print("debug this function from MacroControlFrame")
        self.tcp_connected = status
        self.update_button_states()

    def update_button_states(self):
        print("debug this function from MacroControlFrame")
        if self.serial_connected and self.tcp_connected:
            self.btn_start.config(state='normal')
        else:
            self.btn_start.config(state='disabled')

    def set_start_time(self):
        print("debug this function from MacroControlFrame")
        self.start_time = datetime.now()
        self.val_start_time.config(text=self.start_time.strftime("%H:%M:%S"))
        print(f"Start time set to: {self.start_time.strftime('%H:%M:%S')}")

    def set_stop_time(self):
        print("debug this function from MacroControlFrame")
        self.stop_time = datetime.now()
        self.val_stop_time.config(text=self.stop_time.strftime("%H:%M:%S"))
        print(f"Stop time set to: {self.stop_time.strftime('%H:%M:%S')}")
        self.macro_running = False  # Clear the flag when the sequence stops
        self.update_elapsed_time()

    def update_elapsed_time(self):
        print("debug this function from MacroControlFrame")
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
        print("debug this function from MacroControlFrame")
        print("Sequence Reset")
        self.macro_running = False  # Ensure the flag is cleared
        self.start_time = None
        self.stop_time = None
        self.val_start_time.config(text="00:00:00")
        self.val_stop_time.config(text="--:--:--")
        self.val_elapsed_time.config(text="--:--:--")
        self.elapsed_time.set("00:00:00")
        self.completed_cycles_value.set(0)
        self.ent_total_cycles.delete(0, tk.END)
        self.ent_total_cycles.insert(0, "105")
        print("Sequence reset")


class StatusFrame(ttk.Frame):
    def __init__(self, master=None, dispatcher=None):
        super().__init__(master)
        self.dispatcher = dispatcher

        # Create a LabelFrame to hold the status labels
        self.status_label_frame = ttk.LabelFrame(self, text="Connection Status")
        self.status_label_frame.grid(row=0, column=0, padx=10, pady=5, sticky="new")

        self.lbl_serial_status = ttk.Label(self.status_label_frame, text="Serial: Disconnected", foreground="dark grey")
        self.lbl_serial_status.grid(row=0, column=0, padx=20, pady=5)

        self.lbl_tcp_status = ttk.Label(self.status_label_frame, text="TCP: Disconnected", foreground="dark grey")
        self.lbl_tcp_status.grid(row=1, column=0, padx=20, pady=0)

        self.lbl_macro_status = ttk.Label(self.status_label_frame, text="Macro: Stopped", foreground="dark grey")
        self.lbl_macro_status.grid(row=2, column=0, padx=20, pady=5)
        """TODO: move these out of here"""
        self.dispatcher.register_event('updateSerialConnectionStatus', self.update_serial_status)
        self.dispatcher.register_event('updateTCPConnectionStatus', self.update_tcp_status)
        self.dispatcher.register_event('updateMacroRunningStatus', self.update_macro_status)

    # UI UPDATES
    def update_serial_status(self, status):
        if status:
            self.lbl_serial_status.config(text="SERIAL: Connected", foreground="green")
        else:
            self.lbl_serial_status.config(text="SERIAL: Closed", foreground="red")

    def update_tcp_status(self, status):
        if status:
            self.lbl_tcp_status.config(text="TCP: Connected", foreground="green")
        else:
            self.lbl_tcp_status.config(text="TCP: Disconnected", foreground="red")

    def update_macro_status(self, status):
        if status:
            self.lbl_macro_status.config(text="MACRO: Running", foreground="green")
        else:
            self.lbl_macro_status.config(text="MACRO: Stopped", foreground="red")
