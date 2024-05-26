import tkinter as tk
from tkinter import ttk


class TCPConfig(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("TCP Configuration")

        # IP Address
        self.ip_address_label = ttk.Label(self, text="IP Address:")
        self.ip_address_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.ip_address_options = ["192.168.0.1", "192.168.0.2", "192.168.0.3", "192.168.0.4", "192.168.0.5"]
        self.ip_address_var = tk.StringVar(value=self.ip_address_options[0])
        self.ip_address_dropdown = ttk.Combobox(self, textvariable=self.ip_address_var, values=self.ip_address_options)
        self.ip_address_dropdown.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

        # Port
        self.port_label = ttk.Label(self, text="Port:")
        self.port_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.port_options = ["80", "443", "8080", "8443"]
        self.port_var = tk.StringVar(value=self.port_options[0])
        self.port_dropdown = ttk.Combobox(self, textvariable=self.port_var, values=self.port_options)
        self.port_dropdown.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        # Protocol
        self.protocol_label = ttk.Label(self, text="Protocol:")
        self.protocol_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.protocol_options = ["TCP", "UDP"]
        self.protocol_var = tk.StringVar(value=self.protocol_options[0])
        self.protocol_dropdown = ttk.Combobox(self, textvariable=self.protocol_var, values=self.protocol_options)
        self.protocol_dropdown.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

        # Connection Timeout
        self.timeout_label = ttk.Label(self, text="Connection Timeout:")
        self.timeout_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.timeout_options = ["5", "10", "15", "20", "30"]
        self.timeout_var = tk.StringVar(value=self.timeout_options[0])
        self.timeout_dropdown = ttk.Combobox(self, textvariable=self.timeout_var, values=self.timeout_options)
        self.timeout_dropdown.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

        # Configure grid
        self.columnconfigure(1, weight=1)


if __name__ == "__main__":
    app = TCPConfig()
    app.mainloop()
