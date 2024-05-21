# control_services.py

import socket
import threading
from datetime import datetime
from tkinter import messagebox
from threading import Thread
import serial


class SerialService:
    def __init__(self, dispatcher=None):
        self.read_thread = None
        self.dispatcher = dispatcher
        self.serial_port = None
        self.serial_port_name = None
        self.baud_rate = 9600
        self.commands = {
            'MTRS': '$24200000000MTRS5E',
            'MALN': '$24200000000MALN0049-102783C',
            'CSOL': '@2400000000016$24200000000MTRS5E',
            'HRST': '@2400000000016',
        }

    @staticmethod
    def get_timestamp():
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def read_from_port(self, serial_port):
        self.serial_port = serial_port
        print(f"Reading from {self.serial_port}.")
        print(f"[{self.get_timestamp()}] Started thread for reading from port.")
        while self.serial_port and self.serial_port.is_open:
            message = self.serial_port.readline().decode('utf-8').strip()
            if message:
                self.dispatcher.emit('logData', f"Received: {message}", self.serial_port_name, 'received')

    def stop_reading(self):
        if self.read_thread and self.read_thread.is_alive():
            self.read_thread.join()

    def send_serial_command(self, command):
        self.dispatcher.emit('logData', f"Sent: {command}", self.serial_port_name, 'sent')
        self.serial_port.write(f"{command}\r\n".encode('utf-8'))

    def connect_serial_port(self, serial_port):
        self.serial_port_name = serial_port
        # Close the previous connection if it exists
        if self.serial_port and self.serial_port.is_open:
            self.close_serial_port(self.serial_port_name)  # Call the close method

        try:
            # Create a new serial connection with error handling
            self.serial_port = serial.Serial(
                self.serial_port_name,
                self.baud_rate,
                timeout=1,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS
            )

            # Emit log and start read thread
            self.dispatcher.emit('logData', self.serial_port_name, f"Opened at {self.baud_rate} baud.", "")
            threading.Thread(
                target=self.read_from_port, args=(self.serial_port,), daemon=True
            ).start()
            self.dispatcher.emit('updateSerialConnectionStatus', True)
            print(f"Serial port {self.serial_port_name} opened and read thread started.")

        except serial.SerialException as e:
            messagebox.showerror(
                "Serial Port Error",
                f"Failed to open serial port {self.serial_port_name}: {e}"
            )
            print(f"Failed to open serial port {self.serial_port_name}: {e}")
            self.dispatcher.emit('updateSerialConnectionStatus', False)

    def close_serial_port(self, serial_port):
        if self.serial_port and self.serial_port.is_open:
            self.serial_port.close()
            self.stop_reading()
            self.dispatcher.emit('logData', self.serial_port_name, f"Closed {serial_port} at {self.baud_rate} baud.", "closed")
            self.dispatcher.emit('updateSerialConnectionStatus', False)
            print(f"Disconnected from {serial_port}")

# COMMANDS
    def move_to_ready_station(self):
        command = self.commands['MTRS']
        print(f"Sending: {command}")
        self.send_serial_command(command)

    def align_wafer(self):
        command = self.commands['MALN']
        print(f"Sending: {command}")
        self.send_serial_command(command)

    def toggle_chuck(self):
        command = self.commands['CSOL']
        print(f"Sending: {command}")
        self.send_serial_command(command)

    def hardware_reset(self):
        command = self.commands['HRST']
        print(f"Sending: {command}")
        self.send_serial_command(command)

    def custom_serial_command(self, custom_command):
        command = custom_command
        print(f"Sending custom command: {command}")
        self.send_serial_command(command)


class TCPService:
    def __init__(self, dispatcher=None):
        self.dispatcher = dispatcher
        self.socket = None
        self.server_socket = None

    def setup_server(self, host, port):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (host, port)
        try:
            self.server_socket.bind(server_address)
            self.dispatcher.emit('logData', f"Server started on {host}:{port}", 'tcp', 'opened')
            Thread(target=self.wait_for_client_connection).start()
        except Exception as e:
            self.dispatcher.emit('logData', f"Error starting server: {e}", 'tcp', 'error')

    def wait_for_client_connection(self):
        self.server_socket.listen(1)
        while True:
            client_socket, client_address = self.server_socket.accept()
            try:
                self.dispatcher.emit('logData', f"Connected to {client_address}", 'tcp', 'opened')
                Thread(target=self.handle_client_connection, args=(client_socket,)).start()
            except Exception as e:
                self.dispatcher.emit('logData', f"Error accepting connection: {e}", 'tcp', 'error')

    def handle_client_connection(self, client_socket):
        data = client_socket.recv(1024)
        self.dispatcher.emit('logData', f"Received: {data}", 'tcp', 'received')
        response = "Data received"
        client_socket.sendall(response.encode('utf-8'))
        self.dispatcher.emit('logData', "Response sent", 'tcp', 'sent')

    def connect_tcp_socket(self, ip_address, port, timeout=5.0):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.settimeout(timeout)
            self.socket.connect((ip_address, int(port)))
            self.dispatcher.emit('logData', f"Connected to {ip_address}:{port}", 'tcp', 'opened')
            self.dispatcher.emit('updateTCPConnectionStatus', True)
            print(f"Connected to {ip_address}:{port}")
            return True
        except socket.error as e:
            self.dispatcher.emit('logData', f"Connection timed out {ip_address}:{port}", 'tcp', 'error')
            self.dispatcher.emit('updateTCPConnectionStatus', False)
            print(f"Connection failed to {ip_address}:{port}: {e}")
            return False

    def close_tcp_socket(self, ip_address, port):
        if self.socket:
            self.socket.close()
            self.socket = None
            self.dispatcher.emit('logData', f"Close {ip_address}:{port}", 'tcp', 'closed')
            self.dispatcher.emit('updateTCPConnectionStatus', False)
            print(f"Disconnected from {ip_address}:{port}")

    def send_data(self, data):
        if self.socket:
            try:
                self.socket.sendall(data.encode('utf-8'))
                self.dispatcher.emit('logData', f"Data sent {data}", 'tcp', 'sent')
                print(f"Data sent: {data}")
            except socket.error as e:
                self.dispatcher.emit('logData', f"Data send failed", 'tcp', 'error')
                print(f"Failed to send data: {e}")
        else:
            self.dispatcher.emit('logData', f"TCP not connected", 'tcp', 'error')
            print("No active connection to send data.")

# COMMANDS
    def trigger_one(self):
        command = "T1"
        self.send_data(command)
        print("Triggering T1")

    def trigger_two(self):
        command = "T2"
        self.send_data(command)
        print("Triggering T2")

    def prev_camera(self):
        command = "FW,PV"
        self.send_data(command)
        print("Previous Camera View")

    def next_camera(self):
        command = "FW,NX"
        self.send_data(command)
        print("Next Camera View")

    def get_custom_serial_command(self):
        pass

    @staticmethod
    def send_custom_tcp(command):
        print(f"Sending tcp command: {command}")


class MacroService:
    def __init__(self, dispatcher=None):
        self.dispatcher = dispatcher
        self.total_cycles = 0
        self.completed_cycles = 0
        self.current_step = 0
        self.macro_running = False

    def start_sequence(self):
        print("Starting sequence")
        if not (self.dispatcher.get('serial_connected') and self.dispatcher.get('tcp_connected')):
            self.dispatcher.emit('logData', 'Cannot start sequence: Ensure Serial and TCP connections are active', 'macro', 'error')
            return
        self.total_cycles = int(self.dispatcher.get('total_cycles'))
        self.completed_cycles = 0
        self.current_step = 0
        self.macro_running = True
        self.dispatcher.emit('updateMacroRunningStatus', self.macro_running)
        self.next_step()

    def next_step(self):
        if self.current_step == 0:
            self.dispatcher.emit('moveToReadyStation')
            self.dispatcher.register_event('responseReceived', self.handle_response_mtrs)
        elif self.current_step == 1:
            self.dispatcher.emit('alignWafer')
            self.dispatcher.register_event('responseReceived', self.handle_response_maln)
        print("Stepping through sequence")

    def handle_response_mtrs(self, message):
        if message.startswith('@'):
            self.current_step += 1
            self.next_step()

    def handle_response_maln(self, message):
        if message.startswith('@'):
            self.current_step += 1
            self.dispatcher.after(3000, self.next_step)

    def stop_sequence(self):
        print("Stopping Sequence")
        self.macro_running = False
        self.dispatcher.emit('updateMacroRunningStatus', self.macro_running)

    def reset_sequence(self):
        print("Resetting sequence")
        self.stop_sequence()
        self.total_cycles = 0
        self.completed_cycles = 0
        self.current_step = 0
        self.dispatcher.emit('updateCycleCount', self.total_cycles, self.completed_cycles)

    @staticmethod
    def pause_sequence():
        print("Pausing sequence")

    @staticmethod
    def run_sequence():
        print("Running sequence")

    @staticmethod
    def step_sequence():
        print("not really stepping through sequence")
