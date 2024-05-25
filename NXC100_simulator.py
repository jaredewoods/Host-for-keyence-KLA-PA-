import tkinter as tk
from tkinter import ttk, scrolledtext
import serial
import serial.tools.list_ports
import threading
import time
import socket
import logging
import datetime

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class SerialSimulator:
    def __init__(self, master):
        self.sim_separator0 = None
        self.t1_delay_spinbox = None
        self.t1_delay = None
        self.t1_delay_label = None
        self.read_thread = None
        self.serial_port = None
        self.btn_maln_completed = None
        self.btn_mtrs_completed = None
        self.custom_command_entry = None
        self.btn_maln_response = None
        self.maln_delay_spinbox = None
        self.maln_delay_label = None
        self.btn_send_error_command = None
        self.log_display = None
        self.btn_mtrs_response = None
        self.rad_auto_off = None
        self.rad_auto_on = None
        self.connect_button = None
        self.serial_port_dropdown = None
        self.serial_ports = None
        self.mtrs_delay_spinbox = None
        self.mtrs_delay_label = None
        self.serial_port_var = None
        self.frame = None
        self.std_width = 16
        self.master = master
        self.master.title("NXC100 Simulator")

        self.auto_reply = tk.BooleanVar(value=True)
        self.mtrs_delay = tk.DoubleVar(value=0.5)
        self.maln_delay = tk.DoubleVar(value=1.0)

        self.create_widgets()
        self.grid_widgets()
        self.tcp_server = TCPServer()
        self.start_tcp_server()

    def start_tcp_server(self):
        self.tcp_server = TCPServer(log_callback=self.log_to_display)
        self.tcp_server.start_server()
        self.log_display.insert(tk.END, "Server started at 127.0.0.1:8500\n")

    def stop_tcp_server(self):
        self.tcp_server.stop_server()
        self.log_display.insert(tk.END, "Server stopped 172.0.0.1:8500\n")

    def on_closing(self):
        self.stop_tcp_server()
        if self.serial_port and self.serial_port.is_open:
            self.serial_port.close()
        self.master.destroy()

    def create_widgets(self):
        self.frame = ttk.Frame(self.master, padding="10")

        # Dropdown for serial ports
        self.serial_port_var = tk.StringVar()
        self.serial_ports = self.get_serial_ports()
        self.serial_port_dropdown = ttk.Combobox(self.frame, width=self.std_width - 3,
                                                 textvariable=self.serial_port_var, values=self.serial_ports,
                                                 state='readonly', justify='center')

        # Connect button
        self.connect_button = ttk.Button(self.frame, text="Connect", width=self.std_width,
                                         command=self.connect_serial_port)

        # Radio buttons for auto/manual reply
        self.rad_auto_on = ttk.Radiobutton(self.frame, text=" Auto  ON", variable=self.auto_reply, value=True)
        self.rad_auto_off = ttk.Radiobutton(self.frame, text=" Auto OFF", variable=self.auto_reply, value=False)

        # Spinbox for MTRS delay
        self.mtrs_delay_label = ttk.Label(self.frame, text="MTRS Delay (sec):")
        self.mtrs_delay_spinbox = tk.Spinbox(self.frame, width=self.std_width - 10, from_=0.0, to=1.0, increment=0.1,
                                             textvariable=self.mtrs_delay, format="%.1f", justify='center')

        # Spinbox for MALN delay
        self.maln_delay_label = ttk.Label(self.frame, text="MALN Delay (sec):")
        self.maln_delay_spinbox = tk.Spinbox(self.frame, width=self.std_width - 10, from_=0, to=9, increment=1,
                                             textvariable=self.maln_delay, justify='center')

        # Spinbox for T1 delay
        self.t1_delay_label = ttk.Label(self.frame, text="T1 Delay (sec):")
        self.t1_delay_spinbox = tk.Spinbox(self.frame, width=self.std_width - 10, from_=0.0, to=1.0, increment=0.1, 
                                           textvariable=self.t1_delay, format="%.1f", justify='center')
        
        # Buttons for predefined responses
        self.btn_mtrs_response = ttk.Button(self.frame, width=self.std_width, text="MTRS Resp", command=self.send_mtrs_received)
        self.btn_maln_response = ttk.Button(self.frame, width=self.std_width, text="MALN Resp", command=self.send_maln_received)
        self.btn_mtrs_completed = ttk.Button(self.frame, width=self.std_width, text="MTRS Comp", command=self.send_mtrs_completed)
        self.btn_maln_completed = ttk.Button(self.frame, width=self.std_width, text="MALN Comp", command=self.send_maln_completed)

        # Entry for custom commands
        self.custom_command_entry = ttk.Entry(self.frame, width=self.std_width, justify='center')
        self.custom_command_entry.insert(0, '$24290970000MALN001701085137')
        self.btn_send_error_command = ttk.Button(self.frame, text="Send Error", command=self.send_custom_command)

        self.btn_reset_server_command = ttk.Button(self.frame, text="Reset Server", command=self.send_custom_command)

        # Log display
        self.log_display = scrolledtext.ScrolledText(self.frame, wrap=tk.WORD, width=40, height=12)
        fallback_fonts = ("Consolas", "Courier New", "Lucida Console", "monospace")
        self.log_display.configure(bg="#004000", fg="orange", font=(fallback_fonts, 10))

    def grid_widgets(self):
        self.frame.grid(row=0, column=0, sticky='nsew')
        self.serial_port_dropdown.grid(row=0, column=0, padx=5, pady=5)
        self.connect_button.grid(row=1, column=0, padx=5, pady=5)
        self.rad_auto_on.grid(row=0, column=1, sticky='', padx=(10, 0))
        self.rad_auto_off.grid(row=1, column=1, sticky='', padx=(10, 0))
        self.sim_separator0 = ttk.Separator(orient='horizontal')
        self.sim_separator0.grid(row=2, column=0, columnspan=2, sticky='ew', pady=5, padx=5)
        self.mtrs_delay_label.grid(row=3, column=0, pady=5)
        self.mtrs_delay_spinbox.grid(row=3, column=1, pady=5)
        self.maln_delay_label.grid(row=4, column=0, pady=5)
        self.maln_delay_spinbox.grid(row=4, column=1, pady=5)
        self.t1_delay_label.grid(row=5, column=0, pady=5)
        self.t1_delay_spinbox.grid(row=5, column=1, pady=5)
        self.btn_mtrs_response.grid(row=6, column=0, pady=5)
        self.btn_maln_response.grid(row=6, column=1, pady=5)
        self.btn_mtrs_completed.grid(row=7, column=0, pady=5)
        self.btn_maln_completed.grid(row=7, column=1, pady=5)
        self.custom_command_entry.grid(row=8, column=0, columnspan=2, pady=5, padx=5, sticky='ew')
        self.btn_send_error_command.grid(row=9, column=0, pady=5, padx=5)
        self.btn_reset_server_command.grid(row=9, column=1, pady=5, padx=5)
        self.log_display.grid(row=0, column=2, rowspan=9, pady=5, padx=10, sticky='nsew')

    @staticmethod
    def get_serial_ports():
        ports = serial.tools.list_ports.comports()
        return [port.device for port in ports]

    def connect_serial_port(self):
        selected_port = self.serial_port_var.get()
        self.open_serial_port(selected_port)

    def send_mtrs_received(self):
        response = "@2300000000015"
        self.send_command(response)

    def send_mtrs_completed(self):
        response = "$23200000000MTRS5D"
        self.send_command(response)

    def send_maln_received(self):
        response = "@2100000000013"
        self.send_command(response)

    def send_maln_completed(self):
        response = "$24200000000MALN001701085137"
        self.send_command(response)

    def send_custom_command(self):
        command = self.custom_command_entry.get()
        self.send_command(command)

    def get_auto_response(self, command):
        print(f"received: {command}")
        if command.strip() == "$2MTRSG100ALDD":
            self.send_command("@2300000000015")
            time.sleep(self.mtrs_delay.get())  # Use spinbox value for delay
            self.send_command("$23200000000MTRS5D")
        elif command.strip() == "$2MALN1009000B4":
            self.send_command("@2100000000013")
            print("Starting timer for MALN completed response")
            threading.Timer(self.maln_delay.get(), self.send_maln_completed).start()
        else:
            print(f"No auto-response match for command: {command}")

    def send_command(self, command):
        print(f"send: {command}")
        if not self.serial_port or not self.serial_port.is_open:
            self.log_to_display(f"Error: Serial port not open")
            print("Error: Serial port not open")
            return

        self.serial_port.write(f"{command}\r\n".encode('utf-8'))
        self.log_to_display(f"Sent: {command}")

    def log_to_display(self, message):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        formatted_message = f"{current_time} - {message}\n"
        self.log_display.insert(tk.END, formatted_message)
        self.log_display.see(tk.END)
        print(f"Debug: {formatted_message}")  # Debug print to check if the method is triggered

    def open_serial_port(self, port, baudrate=9600):
        try:
            self.serial_port = serial.Serial(port, baudrate, timeout=1)
            self.read_thread = threading.Thread(target=self.read_from_port, daemon=True)
            self.read_thread.start()
            self.log_to_display(f"Opened serial port {port} at {baudrate} baud.")
        except serial.SerialException as e:
            self.log_to_display(f"Failed to open serial port {port}: {e}")

    def close_serial_port(self):
        if self.serial_port and self.serial_port.is_open:
            self.serial_port.close()
            self.log_to_display(f"Closed serial port.")
            print("Closed serial port.")

    def read_from_port(self):
        while self.serial_port and self.serial_port.is_open:
            try:
                line = self.serial_port.readline().decode('utf-8').strip()
                if line:
                    self.log_to_display(f"Received: {line}")
                    if self.auto_reply.get():
                        self.get_auto_response(line)
                else:
                    pass
            except serial.SerialException as e:
                self.log_to_display(f"Read failed: {e}")
                print(f"Read failed: {e}")

    def check_received_commands(self, received_command):
        print(f"check_received_commands called with: {received_command}")
        clean_command = received_command.strip()
        if clean_command == "$2MTRSG100ALDD":
            self.get_auto_response(clean_command)
        elif clean_command == "$2MALN1009000B4":
            self.get_auto_response(clean_command)

    def close(self):
        self.close_serial_port()
        self.master.destroy()


class TCPServer:
    def __init__(self, host='127.0.0.1', port=8500, log_callback=None):
        self.host = host
        self.port = port
        self.server_socket = None
        self.client_socket = None
        self.is_running = False
        self.log_callback = log_callback

    def start_server(self):
        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(1)
            self.is_running = True
            threading.Thread(target=self.accept_connections, daemon=True).start()
            logging.info("Server started on {}:{}".format(self.host, self.port))
        except Exception as e:
            logging.error("Failed to start server: {}".format(e))

    def accept_connections(self):
        while self.is_running:
            self.client_socket, _ = self.server_socket.accept()
            self.handle_client()

    def handle_client(self):
        while self.is_running:
            try:
                data = self.client_socket.recv(1024).decode('utf-8').strip()  # Strip whitespace here
                if data:
                    self.log_callback(f"Received TCP: {data}")  # Log received data
                    response = self.process_command(data)
                    self.client_socket.sendall(response.encode('utf-8'))
                    self.log_callback(f"Sent TCP: {response}")  # Log sent response
            except (socket.error, AttributeError):
                self.stop_server()

    @staticmethod
    def process_command(command):
        if command.strip() == "T1":
            time.sleep(self.t1_delay.get())  # Use the value from the Spinbox
            return "T1"
        else:
            return command

    def stop_server(self):
        self.is_running = False
        try:
            if self.client_socket:
                self.client_socket.close()
            if self.server_socket:
                self.server_socket.close()
            logging.info("Server stopped")
        except Exception as e:
            logging.error("Error stopping server: {}".format(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = SerialSimulator(root)
    root.protocol("WM_DELETE_WINDOW", app.close)
    root.mainloop()
