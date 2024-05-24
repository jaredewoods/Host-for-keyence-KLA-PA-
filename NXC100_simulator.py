import tkinter as tk
from tkinter import ttk, scrolledtext
import serial
import serial.tools.list_ports
import threading

class SerialSimulator:
    def __init__(self, master):
        self.std_width = 9
        self.master = master
        self.master.title("Serial Command Simulator")

        self.auto_reply = tk.BooleanVar(value=False)
        self.mtrs_delay = tk.DoubleVar(value=0.5)
        self.maln_delay = tk.DoubleVar(value=5.0)

        self.create_widgets()
        self.setup_serial_connection()
        self.grid_widgets()

    def create_widgets(self):
        self.frame = ttk.Frame(self.master, padding="10")

        # Dropdown for serial ports
        self.serial_port_var = tk.StringVar()
        self.serial_ports = self.get_serial_ports()
        self.serial_port_dropdown = ttk.Combobox(self.frame, width=self.std_width + 2, textvariable=self.serial_port_var, values=self.serial_ports, state='readonly')

        # Connect button
        self.connect_button = ttk.Button(self.frame, text="Connect", width=self.std_width, command=self.connect_serial_port)

        # Radio buttons for auto/manual reply
        self.auto_radio = ttk.Radiobutton(self.frame, text="Auto Reply", variable=self.auto_reply, value=True)
        self.manual_radio = ttk.Radiobutton(self.frame, text="Manual Reply", variable=self.auto_reply, value=False)

        # Spinbox for MTRS delay
        self.mtrs_delay_label = ttk.Label(self.frame, text="MTRS Delay (sec):")
        self.mtrs_delay_spinbox = tk.Spinbox(self.frame, width=self.std_width - 6, from_=0.0, to=1.0, increment=0.1, textvariable=self.mtrs_delay, format="%.1f", justify='center')

        # Spinbox for MALN delay
        self.maln_delay_label = ttk.Label(self.frame, text="MALN Delay (sec):")
        self.maln_delay_spinbox = tk.Spinbox(self.frame, width=self.std_width - 6, from_=0, to=9, increment=1, textvariable=self.maln_delay, justify='center')

        # Buttons for predefined responses
        self.btn_mtrs_received = ttk.Button(self.frame, width=self.std_width, text="MTRS Rcvd", command=self.send_mtrs_received)
        self.btn_maln_received = ttk.Button(self.frame, width=self.std_width, text="MALN Rcvd", command=self.send_maln_received)
        self.btn_mtrs_completed = ttk.Button(self.frame, width=self.std_width, text="MTRS Comp", command=self.send_mtrs_completed)
        self.btn_maln_completed = ttk.Button(self.frame, width=self.std_width, text="MALN Comp", command=self.send_maln_completed)

        # Entry for custom commands
        self.custom_command_entry = ttk.Entry(self.frame, width=self.std_width)
        self.send_custom_command_btn = ttk.Button(self.frame, text="Send Custom Command", command=self.send_custom_command)

        # Log display
        self.log_display = scrolledtext.ScrolledText(self.frame, wrap=tk.WORD, width=40, height=20)

    def grid_widgets(self):
        self.frame.grid(row=0, column=0, sticky='nsew')
        self.serial_port_dropdown.grid(row=0, column=0, padx=5, pady=5)
        self.connect_button.grid(row=1, column=0, padx=5, pady=5)
        self.auto_radio.grid(row=0, column=1, sticky='w', padx=(26, 0))
        self.manual_radio.grid(row=1, column=1, sticky='w', padx=(26, 0))
        self.mtrs_delay_label.grid(row=2, column=0, pady=5)
        self.mtrs_delay_spinbox.grid(row=3, column=0, pady=5)
        self.maln_delay_label.grid(row=2, column=1, pady=5)
        self.maln_delay_spinbox.grid(row=3, column=1, pady=5)
        self.btn_mtrs_received.grid(row=4, column=0, pady=5)
        self.btn_maln_received.grid(row=4, column=1, pady=5)
        self.btn_mtrs_completed.grid(row=5, column=0, pady=5)
        self.btn_maln_completed.grid(row=5, column=1, pady=5)
        self.custom_command_entry.grid(row=6, column=0, columnspan=2, pady=5, padx=10, sticky='ew')
        self.send_custom_command_btn.grid(row=7, column=0, columnspan=2, pady=5)
        self.log_display.grid(row=8, column=0, columnspan=2, pady=5)

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

    def get_auto_response(self, command):
        print(f"get_auto_response called with command: {command}")
        if command.strip() == "$2MTRSG100ALDD":
            print("Matched MTRS command")
            # Immediately send MTRS received and completed
            self.send_command("@2300000000015")
            time.sleep(self.mtrs_delay.get())  # Use spinbox value for delay
            self.send_command("$23200000000MTRS5D")
        elif command.strip() == "$2MALN1009000B4":
            print("Matched MALN command")
            # Immediately send MALN received and wait for spinbox value to send completed
            self.send_command("@2100000000013")
            print("Starting timer for MALN completed response")
            threading.Timer(self.maln_delay.get(), self.send_maln_completed).start()
        else:
            print(f"No auto-response match for command: {command}")

    def send_command(self, command):
        print(f"send_command called with command: {command}")
        if not self.serial_port or not self.serial_port.is_open:
            self.log_to_display(f"Error: Serial port not open")
            print("Error: Serial port not open")
            return

        self.serial_port.write(f"{command}\r\n".encode('utf-8'))
        self.log_to_display(f"Sent: {command}")
        print(f"Sent: {command}")

    def log_to_display(self, message):
        self.log_display.insert(tk.END, f"{message}\n")
        self.log_display.see(tk.END)
        print(message)

    def open_serial_port(self, port, baudrate=9600):
        try:
            self.serial_port = serial.Serial(port, baudrate, timeout=1)
            self.read_thread = threading.Thread(target=self.read_from_port, daemon=True)
            self.read_thread.start()
            self.log_to_display(f"Opened serial port {port} at {baudrate} baud.")
            print(f"Opened serial port {port} at {baudrate} baud.")
        except serial.SerialException as e:
            self.log_to_display(f"Failed to open serial port {port}: {e}")
            print(f"Failed to open serial port {port}: {e}")

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
                    print(f"Read from port: {line}")
                    self.log_to_display(f"Received: {line}")
                    if self.auto_reply.get():
                        print(f"Auto reply is enabled, processing command: {line}")
                        self.get_auto_response(line)
                else:
                    print("No data read from port.")
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

if __name__ == "__main__":
    root = tk.Tk()
    app = SerialSimulator(root)
    root.protocol("WM_DELETE_WINDOW", app.close)
    root.mainloop()
