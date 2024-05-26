import tkinter as tk
from tkinter import ttk


class ConfigWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simulator Configuration")

        # Serial Port
        self.serial_port_label = ttk.Label(self, text="Serial Port:")
        self.serial_port_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.serial_port_options = ["COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9", "COM10"]
        self.serial_port_var = tk.StringVar(value=self.serial_port_options[0])
        self.serial_port_dropdown = ttk.Combobox(self, textvariable=self.serial_port_var, values=self.serial_port_options, state='readonly')
        self.serial_port_dropdown.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

        # Baud Rate
        self.baud_rate_label = ttk.Label(self, text="Baud Rate:")
        self.baud_rate_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.baud_rate_options = ["9600", "14400", "19200", "38400", "57600", "115200"]
        self.baud_rate_var = tk.StringVar(value=self.baud_rate_options[0])
        self.baud_rate_dropdown = ttk.Combobox(self, textvariable=self.baud_rate_var, values=self.baud_rate_options, state='readonly')
        self.baud_rate_dropdown.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        # Auto Reply
        self.auto_reply_label = ttk.Label(self, text="Auto Reply:")
        self.auto_reply_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.auto_reply_options = ["On", "Off"]
        self.auto_reply_var = tk.StringVar(value=self.auto_reply_options[0])
        self.auto_reply_dropdown = ttk.Combobox(self, textvariable=self.auto_reply_var, values=self.auto_reply_options, state='readonly')
        self.auto_reply_dropdown.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

        # MTRS Delay
        self.mtrs_delay_label = ttk.Label(self, text="MTRS Delay (sec):")
        self.mtrs_delay_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.mtrs_delay_var = tk.DoubleVar(value=0.5)
        self.mtrs_delay_spinbox = ttk.Spinbox(self, from_=0.0, to=10.0, increment=0.1, textvariable=self.mtrs_delay_var)
        self.mtrs_delay_spinbox.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

        # MALN Delay
        self.maln_delay_label = ttk.Label(self, text="MALN Delay (sec):")
        self.maln_delay_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.maln_delay_var = tk.DoubleVar(value=1.0)
        self.maln_delay_spinbox = ttk.Spinbox(self, from_=0.0, to=10.0, increment=0.1, textvariable=self.maln_delay_var)
        self.maln_delay_spinbox.grid(row=4, column=1, padx=10, pady=5, sticky="ew")

        # Configure grid
        self.columnconfigure(1, weight=1)


if __name__ == "__main__":
    app = ConfigWindow()
    app.mainloop()
