import tkinter as tk
from tkinter import ttk, scrolledtext
import serial
import serial.tools.list_ports
import threading
import time

class SerialSimulator:
    def __init__(self, master):
        self.master = master
        self.master.title("Serial Command Simulator")

        self.auto_reply = tk.BooleanVar(value=False)

        self.create_widgets()
        self.setup_serial_connection()

    def create_widgets(self):
        frame = ttk.Frame(self.master, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Dropdown for serial ports
        self.serial_port_var = tk.StringVar()
        self.serial_ports = self.get_serial_ports()
        self.serial_port_dropdown = ttk.Combobox(frame, textvariable=self.serial_port_var, values=self.serial_ports, state='readonly')
        self.serial_port_dropdown.grid(row=0, column=0, padx=5, pady=5)
        self.serial_port_dropdown.current(0)

        # Connect button
        self.connect_button = ttk.Button(frame, text="Connect", command=self.connect_serial_port)
        self.connect_button.grid(row=0, column=1, padx=5, pady=5)

        # Radio buttons for auto/manual reply
        self.auto_radio = ttk.Radiobutton(frame, text="Auto Reply", variable=self.auto_reply, value=True)
        self.auto_radio.grid(row=1, column=0, sticky=tk.W)
        self.manual_radio = ttk.Radiobutton(frame, text="Manual Reply", variable=self.auto_reply, value=False)
        self.manual_radio.grid(row=1, column=1, sticky=tk.W)

        # Buttons for predefined responses
        self.btn_mtrs_received = ttk.Button(frame, text="MTRS Received", command=self.send_mtrs_received)
        self.btn_mtrs_received.grid(row=2, column=0, pady=5)

        self.btn_maln_received = ttk.Button(frame, text="MALN Received", command=self.send_maln_received)
        self.btn_maln_received.grid(row=2, column=1, pady=5)

        self.btn_mtrs_completed = ttk.Button(frame, text="MTRS Completed", command=self.send_mtrs_completed)
        self.btn_mtrs_completed.grid(row=3, column=0, pady=5)

        self.btn_maln_completed = ttk.Button(frame, text="MALN Completed", command=self.send_maln_completed)
        self.btn_maln_completed.grid(row=3, column=1, pady=5)

        # Entry for custom commands
        self.custom_command_entry = ttk.Entry(frame, width=50)
        self.custom_command_entry.grid(row=4, column=0, columnspan=2, pady=5)
        self.send_custom_command_btn = ttk.Button(frame, text="Send Custom Command", command=self.send_custom_command)
        self.send_custom_command_btn.grid(row=4, column=2, pady=5)

        # Log display
        self.log_display = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=80, height=20)
        self.log_display.grid(row=5, column=0, columnspan=3, pady=5)

    def get_serial_ports(self):
        ports = serial.tools.list_ports.comports()
        return [port.device for port in ports]

    def setup_serial_connection(self):
        self.serial_port = None
        self.read_thread = None

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

    def send_command(self, command):
        if not self.serial_port or not self.serial_port.is_open:
            self.log_to_display("Error: Serial port not open")
            return

        self.serial_port.write(f"{command}\r".encode('utf-8'))
        self.log_to_display(f"Sent: {command}")

        if self.auto_reply.get():
            auto_response = self.get_auto_response(command)
            if auto_response:
                self.serial_port.write(f"{auto_response}\r".encode('utf-8'))
                self.log_to_display(f"Received: {auto_response}")

    def get_auto_response(self, command):
        if command == "$2MTRSG100ALDD":
            # MTRS received and completed immediately
            self.send_command("@2300000000015")
            self.send_command("$23200000000MTRS5D")
        elif command == "$2MALN109000B4":
            # MALN received and completed after delay
            self.send_command("@2100000000013")
            threading.Timer(5, lambda: self.send_command("$24200000000MALN001701085137")).start()
        return None

    def log_to_display(self, message):
        self.log_display.insert(tk.END, f"{message}\n")
        self.log_display.see(tk.END)

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

    def read_from_port(self):
        while self.serial_port and self.serial_port.is_open:
            try:
                line = self.serial_port.readline().decode('utf-8').strip()
                if line:
                    self.log_to_display(f"Received: {line}")
                    if self.auto_reply.get():
                        self.get_auto_response(line)
            except serial.SerialException as e:
                self.log_to_display(f"Read failed: {e}")

    def close(self):
        self.close_serial_port()
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = SerialSimulator(root)
    root.protocol("WM_DELETE_WINDOW", app.close)
    root.mainloop()
