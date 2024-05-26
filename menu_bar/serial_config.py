import tkinter as tk
from tkinter import ttk


class SerialPortConfig(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Serial Port Configuration")

        # Port
        self.port_label = ttk.Label(self, text="Port:")
        self.port_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.port_options = ["COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9", "COM10"]
        self.port_var = tk.StringVar(value=self.port_options[0])
        self.port_dropdown = ttk.Combobox(self, textvariable=self.port_var, values=self.port_options)
        self.port_dropdown.grid(row=0, column=1, padx=10, pady=5, sticky="")

        # Baud Rate
        self.baud_rate_label = ttk.Label(self, text="Baud Rate:")
        self.baud_rate_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.baud_rate_options = ["9600", "14400", "19200", "38400", "57600", "115200"]
        self.baud_rate_var = tk.StringVar(value=self.baud_rate_options[0])
        self.baud_rate_dropdown = ttk.Combobox(self, textvariable=self.baud_rate_var, values=self.baud_rate_options)
        self.baud_rate_dropdown.grid(row=1, column=1, padx=10, pady=5, sticky="")

        # Data Bits
        self.data_bits_label = ttk.Label(self, text="Data Bits:")
        self.data_bits_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.data_bits_options = ["5", "6", "7", "8"]
        self.data_bits_var = tk.StringVar(value=self.data_bits_options[3])
        self.data_bits_dropdown = ttk.Combobox(self, textvariable=self.data_bits_var, values=self.data_bits_options)
        self.data_bits_dropdown.grid(row=2, column=1, padx=10, pady=5, sticky="")

        # Parity
        self.parity_label = ttk.Label(self, text="Parity:")
        self.parity_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.parity_options = ["None", "Even", "Odd", "Mark", "Space"]
        self.parity_var = tk.StringVar(value=self.parity_options[0])
        self.parity_dropdown = ttk.Combobox(self, textvariable=self.parity_var, values=self.parity_options)
        self.parity_dropdown.grid(row=3, column=1, padx=10, pady=5, sticky="")

        # Stop Bits
        self.stop_bits_label = ttk.Label(self, text="Stop Bits:")
        self.stop_bits_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.stop_bits_options = ["1", "1.5", "2"]
        self.stop_bits_var = tk.StringVar(value=self.stop_bits_options[0])
        self.stop_bits_dropdown = ttk.Combobox(self, textvariable=self.stop_bits_var, values=self.stop_bits_options)
        self.stop_bits_dropdown.grid(row=4, column=1, padx=10, pady=5, sticky="")

        # Configure grid
        self.columnconfigure(1, weight=1)


if __name__ == "__main__":
    app = SerialPortConfig()
    app.mainloop()
