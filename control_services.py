# control_services.py
"""TODO: the received response trigger the next step on the macro when it is not even running"""
import socket
import threading
from datetime import datetime
from tkinter import messagebox
import serial
import tkinter as tk
from alarms import alarm_dict
# import winsound


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
        self.response_callback = None

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
                if self.response_callback:
                    self.response_callback(line)

    def stop_reading(self):
        if self.read_thread and self.read_thread.is_alive():
            self.read_thread.join()

    def send_serial_command(self, command, callback=None):
        print(f"Sending command: {command}")
        self.dispatcher.emit('logToDisplay', f"Sent: {command}", self.serial_port_name)
        self.serial_port.write(f"{command}\r\n".encode('utf-8'))
        self.response_callback = callback

    def connect_serial_port(self, serial_port):
        self.serial_port_name = serial_port
        print(f"Connecting to serial port: {self.serial_port_name}")
        if self.serial_port and self.serial_port.is_open:
            self.close_serial_port(self.serial_port_name)

        try:
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
            print(f"Serial port error: {e}")
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

    def send_tcp_data(self, tcp_data):
        if self.socket:
            try:
                self.socket.sendall(tcp_data.encode('utf-8'))
                self.dispatcher.emit('logToDisplay', f"Data sent: {tcp_data}", 'TCP', 'sent')
                print(f"Data sent: {tcp_data}")
                # After sending data, wait for response
                self.handle_received_data()
            except socket.error as e:
                self.dispatcher.emit('logToDisplay', f"Data send failed", 'TCP', 'error')
                print(f"Failed to send data: {e}")
        else:
            self.dispatcher.emit('logToDisplay', f"not connected", 'TCP', 'error')
            messagebox.showwarning('Warning', "No active TCP connection to send data.")

    def handle_received_data(self):
        try:
            data = self.socket.recv(1024).decode('utf-8')
            self.dispatcher.emit('logToDisplay', f"Data received: {data}", 'TCP', 'received')
            print(f"Data received: {data}")
            # Process the received message
            self.handle_response(data)
        except socket.timeout:
            self.dispatcher.emit('logToDisplay', "Data receive timeout", 'TCP', 'error')
            print("Receive timeout")
            self.dispatcher.emit('handleResponseT1')
        except socket.error as e:
            self.dispatcher.emit('logToDisplay', f"Data receive failed: {e}", 'TCP', 'error')
            print(f"Failed to receive data: {e}")
            self.dispatcher.emit('handleResponseT1')

    def handle_response(self, data):
        data = data.strip()
        if data == "T1":
            print("Received expected response: T1")
            self.dispatcher.emit('logToDisplay', "Received expected response: T1", 'TCP', 'info')
            self.dispatcher.emit('handleResponseT1')
        else:
            self.dispatcher.emit('logToDisplay', f"Unexpected response: {data}", 'TCP', 'error')
            print(f"Unexpected response: {data}")
            self.dispatcher.emit('handleResponseT1')

    # COMMANDS
    def trigger_one(self):
        command = "T1\r\n"
        self.send_tcp_data(command)
        print("Triggering T1")

    def trigger_two(self):
        command = "T2\r\n"
        self.send_tcp_data(command)
        print("Triggering T2")

    def prev_camera(self):
        command = "FW,PV\r\n"
        self.send_tcp_data(command)
        print("Previous Camera View")

    def next_camera(self):
        command = "FW,NX\r\n"
        self.send_tcp_data(command)
        print("Next Camera View")

    def get_custom_serial_command(self):
        pass

    @staticmethod
    def send_custom_tcp(command):
        print(f"Sending tcp command: {command}")


class MacroService:
    def __init__(self, dispatcher=None, serial_service=None):
        self.dispatcher = dispatcher
        self.serial_service = serial_service
        self.macro_running = False
        self.total_cycles = 10
        self.completed_cycles = 0

    def initialize_sequence(self):
        print("Initializing Sequence")
        self.macro_running = True
        self.dispatcher.emit('updateMacroRunningStatus', self.macro_running)
        self.completed_cycles = 0
        self.run_sequence()

    def run_sequence(self):
        if self.macro_running:
            print("Running sequence")
            self.send_command_mtrs()

    def send_command_mtrs(self):
        print("Sending command: MTRS")
        self.dispatcher.emit('moveToReadyPosition')
        self.serial_service.send_serial_command(self.serial_service.commands['MTRS'], self.handle_response_mtrs)

    def handle_response_mtrs(self, message):
        if '@' in message:
            print("MTRS acknowledgement received")
        if '$' in message:
            mtrs_index = message.find('MTRS')
            if mtrs_index >= 8:
                pre_mtrs = message[mtrs_index - 8:mtrs_index]
                if pre_mtrs == '00000000':
                    print("MTRS positive completion received")
                    self.send_command_maln()
                else:
                    alarm = pre_mtrs[:4]
                    subcode = pre_mtrs[4:]
                    self.show_alarm_messagebox(alarm, subcode)
                    print("MTRS alarm received")

    def send_command_maln(self):
        print("Sending command: MALN")
        self.serial_service.send_serial_command(self.serial_service.commands['MALN'], self.handle_response_maln)

    def handle_response_maln(self, message):
        if '@' in message:
            print("MALN acknowledgement received")
        if '$' in message:
            maln_index = message.find('MALN')
            if maln_index >= 8:
                pre_mtrs = message[maln_index - 8:maln_index]
                if pre_mtrs == '00000000':
                    print("MALN positive completion received")
                    self.wait_3_seconds()
                else:
                    alarm = pre_mtrs[:4]
                    subcode = pre_mtrs[4:]
                    self.show_alarm_messagebox(alarm, subcode)
                    print("MALN alarm received")

    def wait_3_seconds(self):
        print("Waiting for 3 seconds")
        threading.Timer(3, self.send_command_t1).start()

    def send_command_t1(self):
        print("Sending command: T1")
        self.dispatcher.emit('triggerOne')

    def handle_response_t1(self):
        print("Acknowledgment received for T1")
        self.dispatcher.emit('incrementCycleCount')

    def increment_cycle_count(self):
        self.completed_cycles += 1
        print(f"Emitting updateCompletedCycles event with value: {self.completed_cycles}")
        self.dispatcher.emit("updateCompletedCycles", self.completed_cycles)
        print(f"New cycle count: {self.completed_cycles}")
        if self.completed_cycles >= self.total_cycles:
            print("Total cycles reached, stopping sequence")
            self.stop_sequence()
        else:
            threading.Timer(0.1, self.run_sequence).start()

    def stop_sequence(self):
        print("Stopping Sequence")
        self.macro_running = False
        self.dispatcher.emit('updateMacroRunningStatus', self.macro_running)

    def reset_sequence(self):
        print("Resetting sequence")
        self.completed_cycles = 0
        self.macro_running = False

    def show_alarm_messagebox(self, alarm, subcode):
        alarm_data = alarm_dict.get(alarm, None)

        if alarm_data is None:
            alarm_info = {
                "Message": "Unknown message",
            }
        else:
            alarm_info = next(iter(alarm_data.values()), {
                "Message": "Unknown message",
                "Cause": "Unknown cause",
                "Potential Causes": ["Unknown potential causes"]
            })

        message = alarm_info.get("Message", "Unknown message")
        cause = alarm_info.get("Cause", "Unknown cause")
        potential_causes = alarm_info.get("Potential Causes", ["Unknown potential causes"])
        potential_causes_formatted = "\n".join([f"• {cause}" for cause in potential_causes])
        formatted_message = (
            f"Alarm: {alarm}\n\n"
            f"{message}\n\n"
            f"{cause}\n\n"
            f"Potential Causes:\n{potential_causes_formatted}\n\n"
            f"Subcode: {subcode}"
        )

        # winsound.Beep(1000, 1000)
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Alarm", formatted_message)
        root.destroy()
