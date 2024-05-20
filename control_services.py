# control_services.py

import socket
import threading
from datetime import datetime
from tkinter import messagebox
import serial


class SerialService:
    def __init__(self, dispatcher=None):
        self.read_thread = None
        self.dispatcher = dispatcher
        self.serial_port = None
        self.serial_port_name = None
        self.baud_rate = 9600
        self.commands = {
            'MTRS': '$2MTRSG100ALDD',
            'MALN': '$2MALN1009000B4',
            'CSOL': '$2CSOLA0D4',
            'HRST': '$1HRST72',
        }

    @staticmethod
    def get_timestamp():
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def read_from_port(self, serial_port):
        self.serial_port = serial_port
        print(f"Reading from {self.serial_port}.")
        print(f"[{self.get_timestamp()}] Started thread for reading from port.")

        while self.serial_port and self.serial_port.is_open:
            line = self.serial_port.readline().decode('utf-8').strip()  # Read a line
            if line:
                timestamp = self.get_timestamp()
                print(f"Complete message received: {line}")
                self.dispatcher.emit('receivedData', line, self.serial_port_name)
                self.dispatcher.emit('logToDisplay', f"Received: {line}", self.serial_port_name)

    def stop_reading(self):
        if self.read_thread and self.read_thread.is_alive():
            self.read_thread.join()

    def send_serial_command(self, command):
        print(f"Sending command: {command}")  # Debug: Show sent command
        self.dispatcher.emit('logToDisplay', f"Sent: {command}", self.serial_port_name)
        self.serial_port.write(f"{command}\r\n".encode('utf-8'))

    def connect_serial_port(self, serial_port):
        self.serial_port_name = serial_port
        print(f"Connecting to serial port: {self.serial_port_name}")  # Debug: Show connection attempt
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
            print(f"Serial port {self.serial_port_name} opened at {self.baud_rate} baud.")  # Debug: Show connection success
            self.dispatcher.emit('logToDisplay', self.serial_port_name, f"Opened at {self.baud_rate} baud.", "")
            threading.Thread(
                target=self.read_from_port, args=(self.serial_port,), daemon=True
            ).start()
            self.dispatcher.emit('updateSerialConnectionStatus', True)
            print(f"Serial port {self.serial_port_name} opened and read thread started.")

        except serial.SerialException as e:
            print(f"Serial port error: {e}")  # Debug: Show connection error
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
            self.dispatcher.emit('logToDisplay', self.serial_port_name, f"Closed {serial_port} at {self.baud_rate} baud.", "closed")
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

    def connect_tcp_socket(self, ip_address, port, timeout=5.0):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.settimeout(timeout)
            self.socket.connect((ip_address, int(port)))
            self.dispatcher.emit('logToDisplay', f"Connected to {ip_address}:{port}", 'tcp', 'opened')
            self.dispatcher.emit('updateTCPConnectionStatus', True)
            print(f"Connected to {ip_address}:{port}")
            return True
        except socket.error as e:
            self.dispatcher.emit('logToDisplay', f"Connection timed out {ip_address}:{port}", 'tcp', 'error')
            self.dispatcher.emit('updateTCPConnectionStatus', False)
            print(f"Connection failed to {ip_address}:{port}: {e}")
            return False

    def close_tcp_socket(self, ip_address, port):
        if self.socket:
            self.socket.close()
            self.socket = None
            self.dispatcher.emit('logToDisplay', f"Close {ip_address}:{port}", 'tcp', 'closed')
            self.dispatcher.emit('updateTCPConnectionStatus', False)
            print(f"Disconnected from {ip_address}:{port}")

    def send_data(self, data):
        if self.socket:
            try:
                self.socket.sendall(data.encode('utf-8'))
                self.dispatcher.emit('logToDisplay', f"Data sent {data}", 'tcp', 'sent')
                print(f"Data sent: {data}")
            except socket.error as e:
                self.dispatcher.emit('logToDisplay', f"Data send failed", 'tcp', 'error')
                print(f"Failed to send data: {e}")
        else:
            self.dispatcher.emit('logToDisplay', f"TCP not connected", 'tcp', 'error')
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
        self.macro_running = False
        self.cycle_count = 0
        self.total_cycles = 105

    def handle_received_data(self, message, port_name):
        print(f"Received data from {port_name}: {message}")
        # Determine the command the response corresponds to and handle it
        if 'MTRS' in message:
            self.handle_response_mtrs(message)
        elif 'MALN' in message:
            self.handle_response_maln(message, port_name)

    def initialize_sequence(self):
        print("Initializing Sequence")
        self.macro_running = True
        self.dispatcher.emit('updateMacroRunningStatus', self.macro_running)
        "TODO: should have total cycles retrieve the user entry"
        try:
            self.total_cycles = int(105)
        except ValueError:
            print("Total Cycles Entry field value has to be an integer")
            return
        self.update_cycle_count()

    def update_cycle_count(self):
        cycle_count = self.total_cycles
        print(f"Current cycle count: {cycle_count}")
        self.run_sequence()

    def run_sequence(self):
        print("Running sequence")
        if self.macro_running:
            self.send_command_mtrs()
        else:
            print("Sequence Stopped")

    def send_command_mtrs(self):
        print("Sending command: MTRS")
        self.dispatcher.emit('moveToReadyStation')

    def handle_response_mtrs(self, combined_response):
        print(f"Handling response for MTRS: {combined_response}")
        try:
            receipt_response, completion_response = self.split_response(combined_response)
            print(f"Receipt response: {receipt_response}")
            print(f"Completion response: {completion_response}")
            if receipt_response and completion_response:
                receipt_data = self.parse_receipt_response(receipt_response)
                print(f"Receipt Acknowledgment: {receipt_data}")
                completion_data = self.parse_completion_response_mtrs(completion_response)
                print(f"Completion Status: {completion_data}")

                # Handle success and error based on alarm and subcodes
                if completion_data['alarm_code'] == '0000':
                    print("MTRS command completed successfully")
                    self.dispatcher.emit('command_success', completion_data)
                    self.send_command_maln()  # Continue to next command
                else:
                    print(f"MTRS command failed with alarm code: {completion_data['alarm_code']}")
                    self.dispatcher.emit('command_failure', completion_data)
            else:
                print("Invalid combined MTRS response format")
                self.dispatcher.emit('handle_error', 'Invalid combined MTRS response format')
        except Exception as e:
            print(f"Error handling MTRS response: {e}")
            self.dispatcher.emit('handle_error', str(e))

    def send_command_maln(self):
        print("Sending command: MALN")
        self.dispatcher.emit('alignWafer')

    def handle_response_maln(self, message, serial_port_name):
        print(f"Handling response for MALN: {message}")
        try:
            if message.startswith('$2') and 'MALN' in message:
                parts = message.split('MALN')
                if len(parts) == 2:
                    response_data = parts[1]
                    print(f"Response data: {response_data}")

                    receipt_response = response_data[:4]  # Example: First 4 characters
                    completion_response = response_data[4:]  # Example: Remaining characters

                    print(f"Receipt response: {receipt_response}")
                    print(f"Completion response: {completion_response}")

                    if receipt_response and completion_response:
                        print("Valid MALN response received")
                        self.dispatcher.emit('logToDisplay', f"MALN response: {message}", serial_port_name, 'received')
                        self.wait_3_seconds()
                    else:
                        print("Invalid MALN response format")
                        self.dispatcher.emit('handle_error', "Invalid MALN response format")
                else:
                    print("Invalid combined MALN response format")
                    self.dispatcher.emit('handle_error', "Invalid combined MALN response format")
            else:
                print("Unexpected MALN response format")
                self.dispatcher.emit('handle_error', "Unexpected MALN response format")
        except Exception as e:
            print(f"Error handling MALN response: {e}")
            self.dispatcher.emit('handle_error', str(e))

    def wait_3_seconds(self):
        print("Waiting for 3 seconds")
        threading.Timer(0.3, self.send_command_t1).start()

    def send_command_t1(self):
        print("Sending command: T1")
        self.dispatcher.emit('triggerOne')

    def handle_response_t1(self, message):
        print(f"Handling response for T1: {message}")
        if message == 'ACK':
            print("Acknowledgment received for T1")
            self.dispatcher.emit('incrementCycleCount')
        else:
            print("Error handling T1 response")
            """TODO: handle_error doesn't exist"""
            self.dispatcher.emit('handle_error', 'T1 error')

    def increment_cycle_count(self):
        print("Incrementing cycle count")
        self.cycle_count += 1
        print(f"New cycle count: {self.cycle_count}")
        self.dispatcher.emit('update_cycle_count', self.cycle_count)
        if self.cycle_count >= self.total_cycles:
            print("Total cycles reached, stopping sequence")
            self.stop_sequence()
        else:
            print("Total cycles not reached, waiting for 0.1 seconds before repeating")
            threading.Timer(0.1, self.run_sequence).start()

    def stop_sequence(self):
        print("Stopping Sequence")
        self.macro_running = False
        self.dispatcher.emit('updateMacroRunningStatus', self.macro_running)

    def reset_sequence(self):
        print("Resetting sequence")
        self.cycle_count = 0
        self.macro_running = False

    def split_response(self, combined_response):
        if '@' in combined_response and '$' in combined_response:
            receipt_index = combined_response.index('@')
            completion_index = combined_response.index('$', receipt_index)
            receipt_part = combined_response[receipt_index:completion_index].strip()
            completion_part = combined_response[completion_index:].strip()
            return receipt_part, completion_part
        return None, None

    def parse_receipt_response(self, receipt_response):
        if receipt_response.startswith('@'):
            # Example: '@2100000000013'
            unit_number = receipt_response[1:2]
            status_code = receipt_response[2:4]  # Ignored for now
            alarm_code = receipt_response[4:8]
            alarm_subcode = receipt_response[8:12]
            checksum = receipt_response[12:]  # Ignored
            return {
                'unit_number': unit_number,
                'status_code': status_code,
                'alarm_code': alarm_code,
                'alarm_subcode': alarm_subcode,
                'checksum': checksum
            }
        raise ValueError("Invalid receipt response format")

    def parse_completion_response_mtrs(self, completion_response):
        if completion_response.startswith('$'):
            # Example: '$23200000000MTRS5D'
            unit_number = completion_response[1:2]
            status_code = completion_response[2:4]  # Ignored for now
            alarm_code = completion_response[4:8]
            alarm_subcode = completion_response[8:12]
            completed_command = completion_response[12:16]
            checksum = completion_response[16:]  # Ignored
            return {
                'unit_number': unit_number,
                'status_code': status_code,
                'alarm_code': alarm_code,
                'alarm_subcode': alarm_subcode,
                'completed_command': completed_command,
                'checksum': checksum
            }
        raise ValueError("Invalid MTRS completion response format")

    def parse_completion_response_maln(self, completion_response):
        if completion_response.startswith('$'):
            # Example: '$24200000000MALN001701085137'
            unit_number = completion_response[1:2]
            status_code = completion_response[2:4]  # Ignored for now
            alarm_code = completion_response[4:8]
            alarm_subcode = completion_response[8:12]
            completed_command = completion_response[12:16]
            offset_distance = completion_response[16:20]
            offset_angle = completion_response[20:26]
            checksum = completion_response[26:]  # Ignored
            return {
                'unit_number': unit_number,
                'status_code': status_code,
                'alarm_code': alarm_code,
                'alarm_subcode': alarm_subcode,
                'completed_command': completed_command,
                'offset_distance': offset_distance,
                'offset_angle': offset_angle,
                'checksum': checksum
            }
        raise ValueError("Invalid MALN completion response format")
