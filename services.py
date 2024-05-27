# services.py

import socket
import threading
import tkinter as tk
from tkinter import messagebox
import serial
import time
from resources.alarms import alarm_dict


class SerialService:
    def __init__(self, dispatcher=None):
        self.dispatcher = dispatcher
        self.read_thread = None
        self.serial_port = None
        self.serial_port_name = None
        self.baud_rate = 9600
        self.commands = {
            'MTRS': '$2MTRSG100ALDD',
            'MALN': '$2MALN1009000B4',
            'CSOL': '$2CSOLA0D4',
            'HRST': '$1HRST72',
            'CCLR': '$2CCLRE9B',
        }
        self.response_callback = None

    def connect_serial_port(self, serial_port):
        self.serial_port_name = serial_port

        if self.serial_port and self.serial_port.is_open:
            self.close_serial_port(self.serial_port_name)
            print("Serial port was already open")

        try:
            self.serial_port = serial.Serial(
                self.serial_port_name,
                self.baud_rate,
                timeout=1,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS
            )

            print(f"Serial port {self.serial_port_name} opened at {self.baud_rate} baud.")
            self.dispatcher.emit('logToDisplay', f"at {self.baud_rate} baud.", f"Opened {self.serial_port_name}")
            time.sleep(0.5)
            threading.Thread(target=self.read_from_port, args=(self.serial_port,), daemon=True).start()
            self.dispatcher.emit('updateSerialConnectionStatus', True)
            print(f"Serial port {self.serial_port_name} opened and read thread started.")

        except serial.SerialException as e:
            print(f"Serial port error: {e}")
            messagebox.showerror(
                "Serial Port Error",
                f"Failed to open serial port {self.serial_port_name}: {e}"
            )
            self.dispatcher.emit('updateSerialConnectionStatus', False)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            messagebox.showerror(
                "Serial Port Error",
                f"An unexpected error occurred: {e}"
            )
            self.dispatcher.emit('updateSerialConnectionStatus', False)

    def close_serial_port(self, serial_port):
        if self.serial_port and self.serial_port.is_open:
            time.sleep(0.5)
            self.serial_port.close()
            self.dispatcher.emit('logToDisplay', self.serial_port_name, f"Closed {serial_port} at {self.baud_rate} baud.")
            self.dispatcher.emit('updateSerialConnectionStatus', False)
            print(f"Disconnected from {serial_port}")
            self.stop_reading()

    def stop_reading(self):
        if self.read_thread and self.read_thread.is_alive():
            self.read_thread.join()

    def send_serial_command(self, command, callback=None):
        if self.serial_port is None or not self.serial_port.is_open:
            print("Error: No open port to send command")
            messagebox.showerror("Serial Port Error", "Attempted to send command with no open port.")
            return
        print(f"Sending command: {command}")
        self.dispatcher.emit('logToDisplay', f"Sent: {command}", self.serial_port_name)
        self.serial_port.write(f"{command}\r\n".encode('utf-8'))
        self.response_callback = callback

    def move_to_ready_station(self):
        command = self.commands['MTRS']
        print(f"Sending: {command}")
        self.send_serial_command(command)

    def align_wafer(self):
        command = self.commands['MALN']
        print(f"Sending: {command}")
        self.send_serial_command(command)

    def chuck_hold(self):
        command = self.commands['CSOL']
        print(f"Sending: {command}")
        self.send_serial_command(command)

    def hardware_reset(self):
        command = self.commands['HRST']
        print(f"Sending: {command}")
        self.send_serial_command(command)

    def send_custom_serial(self, custom_command):
        command = custom_command
        print(f"Sending custom command: {command}")
        self.send_serial_command(command)

    def emergency_stop(self):
        self.dispatcher.emit('stopSequence')
        if self.serial_port is None or not self.serial_port.is_open:
            print("Error: No open port to send emergency stop command")
            messagebox.showerror("Serial Port Error", "Attempted to send emergency stop with no open port.")
            return
        command = "$2CEMG4E"
        self.dispatcher.emit('logToDisplay', f"Sent: {command}", self.serial_port_name)
        self.serial_port.write(f"{command}\r\n".encode('utf-8'))
        print("Emergency stop command sent")

    def send_clear_command(self):
        command = self.commands['CCLR']
        print(f"Sending: {command}")
        self.send_serial_command(command)

    def read_from_port(self, serial_port):
        self.serial_port = serial_port
        print(f"Reading from {self.serial_port}.")

        while self.serial_port and self.serial_port.is_open:
            try:
                line = self.serial_port.readline()
                if line:
                    line = line.decode('utf-8').strip()
                    print(f"Complete message received: {line}")
                    if '$' in line and len(line) >= 12:
                        error_code = line[4:12]
                        print(error_code)
                        if error_code != "00000000":
                            alarm_code = line[4:8]
                            print(alarm_code)
                            subcode = line[8:12]
                            print(subcode)
                            print(f"Error detected in response. Alarm: {alarm_code}, Subcode: {subcode}")
                            self.show_alarm_messagebox(alarm_code, subcode)
                            # self.dispatcher.emit('emergencyStop')
                        else:
                            print("Valid response, no errors detected.")
                            self.dispatcher.emit('receivedData', f'Received: {line}', self.serial_port_name)
                            if self.response_callback:
                                self.response_callback(line)
                    else:
                        print("Message format incorrect or too short.")
            except serial.SerialException as e:
                print(f"Read failed: {str(e)}")
            except Exception as e:
                print(f"Unhandled exception: {str(e)}")
                break

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

        root = tk.Toplevel()
        root.withdraw()
        messagebox.showerror("Alarm", formatted_message)
        root.destroy()


class TCPService:
    def __init__(self, dispatcher=None):
        self.port = None
        self.ip_address = None
        self.dispatcher = dispatcher
        self.socket = None

    def connect_tcp_socket(self, ip_address, port, timeout=5.0):
        self.ip_address = ip_address
        self.port = port
        
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.settimeout(timeout)
            self.socket.connect((ip_address, int(port)))
            self.dispatcher.emit('logToDisplay', f"Connected to {ip_address}:{port}", 'TCP')
            self.dispatcher.emit('updateTCPConnectionStatus', True)
            print(f"Connected to {ip_address}:{port}")
            return True
        except socket.error as e:
            self.dispatcher.emit('logToDisplay', f"Connection timed out {ip_address}:{port}", 'TCP')
            self.dispatcher.emit('updateTCPConnectionStatus', False)
            print(f"Connection failed to {ip_address}:{port}: {e}")
            return False

    def close_tcp_socket(self):
        if self.socket:
            self.socket.close()
            self.socket = None
            self.dispatcher.emit('logToDisplay', f"Closed {self.ip_address}:{self.port}", 'TCP')
            self.dispatcher.emit('updateTCPConnectionStatus', False)
            print(f"Disconnected from {self.ip_address}:{self.port}")

    def send_tcp_data(self, tcp_data):
        if self.socket:
            try:
                tcp_data_with_terminator = tcp_data + '\r\n'
                self.socket.sendall(tcp_data_with_terminator.encode('utf-8'))
                self.dispatcher.emit('logToDisplay', f"Data sent: {tcp_data}", 'TCP')
                print(f"Data sent: {tcp_data_with_terminator}")
                self.handle_received_data()
            except socket.error as e:
                self.dispatcher.emit('logToDisplay', f"Data send failed: {e}", 'TCP')
                print(f"Failed to send data: {e}")
                self.dispatcher.emit('updateTCPConnectionStatus', False)
        else:
            self.dispatcher.emit('logToDisplay', f"Not connected", 'TCP')
            self.dispatcher.emit('updateTCPConnectionStatus', False)
            messagebox.showwarning('Warning', "No active TCP connection to send data.")

    def handle_received_data(self):
        if self.socket:
            try:
                data = self.socket.recv(1024).decode('utf-8').strip()
                self.dispatcher.emit('logToDisplay', f"Data received: {data}", 'TCP')
                print(f"Data received: {data}")
                self.handle_response(data)
            except socket.timeout:
                self.dispatcher.emit('logToDisplay', "Data receive timeout", 'TCP')
                print("Receive timeout")
                self.dispatcher.emit('handleResponseT1')
            except socket.error as e:
                self.dispatcher.emit('logToDisplay', f"Data receive failed: {e}", 'TCP')
                print(f"Failed to receive data: {e}")
                self.dispatcher.emit('handleResponseT1')

    def handle_response(self, data):
        data = data.strip()
        if data == "T1":
            print("Received expected response: T1")
            self.dispatcher.emit('handleResponseT1')
        else:
            self.dispatcher.emit('logToDisplay', f"Unexpected response: {data}", 'TCP')
            print(f"Unexpected response: {data}")

    # COMMANDS
    def trigger_one(self):
        command = "T1"
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

    def send_custom_tcp(self, custom_command):
        self.send_tcp_data(custom_command)
        print(f"Sending tcp command: {custom_command}")
        self.dispatcher.emit('logToDisplay', f"Sent: {custom_command}", "TCP")


class MacroService:
    def __init__(self, dispatcher=None, serial_service=None, tcp_service=None):
        self.dispatcher = dispatcher
        self.serial_service = serial_service
        self.tcp_service = tcp_service
        self.macro_running = False
        self.total_cycles = None
        self.completed_cycles = 0
        self.stop_requested = False

    def initialize_sequence(self, total_cycles):
        print("Initializing Sequence")
        self.macro_running = True
        self.stop_requested = False
        self.dispatcher.emit('updateMacroRunningStatus', self.macro_running)
        self.completed_cycles = 0
        self.total_cycles = int(total_cycles)
        self.dispatcher.emit('logToDisplay', f"{total_cycles} Cycles\n\n", 'Initializing Sequence for')
        self.run_sequence()

    def run_sequence(self):
        if self.macro_running and not self.stop_requested:
            print("Running sequence")
            self.dispatcher.emit('logToDisplay', f"{self.total_cycles}=======", f'=======Starting Cycle {self.completed_cycles + 1} of')
            self.send_command_mtrs()

    def stop_sequence(self):
        print("Stopping Sequence")
        self.macro_running = False
        self.stop_requested = True
        self.dispatcher.emit('updateMacroRunningStatus', self.macro_running)

    def reset_sequence(self):
        print("Resetting sequence")
        self.completed_cycles = 0
        self.dispatcher.emit("updateCompletedCycles", self.completed_cycles)
        self.macro_running = False
        self.stop_requested = False

    def send_command_mtrs(self):
        if self.stop_requested:
            return
        print("Sending command: MTRS")
        self.dispatcher.emit('moveToReadyPosition')
        self.serial_service.send_serial_command(self.serial_service.commands['MTRS'], self.handle_response_mtrs)

    def handle_response_mtrs(self, message):
        if self.stop_requested:
            return
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
                    print("MTRS alarm received")
                    pass

    def send_command_maln(self):
        if self.stop_requested:
            return
        print("Sending command: MALN")
        self.serial_service.send_serial_command(self.serial_service.commands['MALN'], self.handle_response_maln)

    def handle_response_maln(self, message):
        if self.stop_requested:
            return
        if '@' in message:
            print("MALN acknowledgement received")
            self.dispatcher.emit('logToDisplay', 'Wafer...', 'Aligning')
        if '$' in message:
            maln_index = message.find('MALN')
            if maln_index >= 8:
                pre_mtrs = message[maln_index - 8:maln_index]
                if pre_mtrs == '00000000':
                    print("MALN positive completion received")
                    distance_start = maln_index + 4
                    distance_raw = message[distance_start:distance_start + 4]
                    try:
                        distance_value = int(distance_raw)
                        distance = f"{distance_value / 100:.2f}"
                    except ValueError:
                        distance = "Invalid distance format"
                    angle_start = distance_start + 4
                    angle_raw = message[angle_start:angle_start + 6]
                    angle_sign = '-' if angle_raw[0] == '-' else ''
                    try:
                        angle_value = int(angle_raw.lstrip('-'))
                        angle = f"{angle_value / 100:.2f}"
                    except ValueError:
                        angle = "Invalid angle format"
                    log_message = f"{distance}mm {angle_sign}{angle}deg"
                    self.dispatcher.emit('logToDisplay', log_message, "Offset:")
                    self.wait_3_seconds()
                else:
                    alarm = pre_mtrs[:4]
                    subcode = pre_mtrs[4:]
                    self.show_alarm_messagebox(alarm, subcode)
                    print("MALN alarm received")
                    pass  # pause the macro

    def wait_3_seconds(self):
        print("Waiting for 3 seconds")
        self.dispatcher.emit('logToDisplay', '3 secs.', 'Waiting for')
        threading.Timer(3, self.send_command_t1).start()

    def send_command_t1(self):
        if self.stop_requested:
            return
        print("Sending command: T1")
        self.dispatcher.emit('triggerOne')

    def handle_response_t1(self):
        if self.stop_requested:
            return
        print("Acknowledgment received for T1")
        self.dispatcher.emit('incrementCycleCount')

    def update_total_cycles(self, new_total):
        try:
            new_total_cycles = int(new_total)
            if new_total_cycles < self.completed_cycles:
                raise ValueError("Total cycles cannot be less than completed cycles.")
            self.total_cycles = new_total_cycles
            print(f"Total cycles updated to: {self.total_cycles}")
            self.dispatcher.emit('logToDisplay', f"Total cycles updated to {self.total_cycles}", "MacroService")
        except ValueError as e:
            print(f"Error updating total cycles: {e}")
            self.dispatcher.emit('logToDisplay', str(e), "MacroService")

    def increment_cycle_count(self):
        if self.stop_requested or self.total_cycles is None:
            return
        self.completed_cycles += 1
        self.dispatcher.emit('logToDisplay', f"{self.completed_cycles} of {self.total_cycles}=======\n\n", "=======Completed Cycle:")
        print(f"Emitting updateCompletedCycles event with value: {self.completed_cycles}")
        self.dispatcher.emit("updateCompletedCycles", self.completed_cycles)
        print(f"New cycle count: {self.completed_cycles}")
        if self.completed_cycles >= int(self.total_cycles):
            print("Total cycles reached, stopping sequence")
            self.dispatcher.emit('logToData', {})
            self.dispatcher.emit("stopSequence")
            self.dispatcher.emit("updateCompletedCycles", self.total_cycles)
            self.show_completion_messagebox()
        else:
            threading.Timer(0.1, self.run_sequence).start()

    def emergency_stop_sequence(self):
        print("Emergency stop triggered")
        self.stop_requested = True
        self.dispatcher.emit('updateMacroRunningStatus', self.macro_running)
        self.dispatcher.emit('logToDisplay', "Emergency stop activated", 'Macro')
        self.macro_running = False
        self.show_emergency_stop_messagebox()

    def show_completion_messagebox(self):
        message = f"{self.completed_cycles} Alignments Completed\nExport Log?"
        root = tk.Toplevel()
        root.withdraw()
        result = messagebox.askyesno("SEQUENCE COMPLETED", message)
        if result:
            self.dispatcher.emit('exportLog')

    def show_emergency_stop_messagebox(self):
        root = tk.Tk()
        root.withdraw()
        response = messagebox.askokcancel("EMERGENCY STOP", "Clear Emergency Stop?")
        if response:
            print("Emergency stop cleared")
            self.dispatcher.emit('sendClearCommand')
        else:
            print("Emergency stop not cleared")
        root.destroy()
