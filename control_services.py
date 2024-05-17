
import datetime
import socket
import serial


class SerialService:
    def __init__(self, dispatcher=None):
        self.dispatcher = dispatcher
        self.serial_port = None
        self.baud_rate = 9600
        self.commands = {
            'MTRS': '$2MTRSG100ALDD',
            'MALN': '$2MALN1009000B4',
            'CSOL': '$2CSOLA0D4',
            'HRST': '$1HRST72',
        }

    def send_serial_command(self, command):
        if self.serial_port.is_open:
            self.dispatcher.emit('logData', command, 'Serial', 'Sent')
            self.serial_port.write(f"{command}\r\n".encode('utf-8'))
        else:
            print("Serial port is not open")

    def connect_serial_port(self, serial_port):
        self.serial_port = serial.Serial(serial_port, self.baud_rate)
        print(f"Connected to {self.serial_port} at {self.baud_rate} baud.")

    def close_serial_port(self, serial_port):
        if self.serial_port and self.serial_port.is_open:
            self.serial_port.close()
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

    def connect_tcp_socket(self, ip_address, port, timeout=5.0):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.settimeout(timeout)
            self.socket.connect((ip_address, int(port)))
            print(f"Connected to {ip_address}:{port}")
            return True
        except socket.error as e:
            print(f"Connection failed to {ip_address}:{port}: {e}")
            return False

    def close_tcp_socket(self, ip_address, port):
        if self.socket:
            self.socket.close()
            self.socket = None
            print(f"Disconnected from {ip_address}:{port}")

    def send_data(self, data):
        if self.socket:
            try:
                self.socket.sendall(data.encode('utf-8'))
                print(f"Data sent: {data}")
            except socket.error as e:
                print(f"Failed to send data: {e}")
        else:
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
    def __init__(self):
        self.data = []

    @staticmethod
    def start_sequence():
        print("Starting sequence")

    @staticmethod
    def stop_sequence():
        print("Stopping Sequence")

    @staticmethod
    def step_sequence():
        print("Stepping through sequence")

    @staticmethod
    def pause_sequence():
        print("Pausing sequence")

    @staticmethod
    def run_sequence():
        print("Running sequence")

    @staticmethod
    def reset_sequence():
        print("Resetting sequence")


class DisplayService:
    def __init__(self, dispatcher=None):
        self.dispatcher = dispatcher


class ConnectionStatusService:
    def __init__(self, dispatcher=None):
        self.dispatcher = dispatcher
