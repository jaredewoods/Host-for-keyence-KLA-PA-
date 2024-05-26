import tkinter as tk
from tkinter import ttk

class MacroConfig(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Macro Configuration")

        # Total Cycles
        self.total_cycles_label = ttk.Label(self, text="Total Cycles:")
        self.total_cycles_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.total_cycles_var = tk.IntVar(value=10)
        self.total_cycles_spinbox = ttk.Spinbox(self, from_=1, to=100, textvariable=self.total_cycles_var)
        self.total_cycles_spinbox.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

        # MTRS Delay
        self.mtrs_delay_label = ttk.Label(self, text="MTRS Delay (sec):")
        self.mtrs_delay_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.mtrs_delay_var = tk.DoubleVar(value=0.5)
        self.mtrs_delay_spinbox = ttk.Spinbox(self, from_=0.0, to=10.0, increment=0.1, textvariable=self.mtrs_delay_var)
        self.mtrs_delay_spinbox.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        # MALN Delay
        self.maln_delay_label = ttk.Label(self, text="MALN Delay (sec):")
        self.maln_delay_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.maln_delay_var = tk.DoubleVar(value=1.0)
        self.maln_delay_spinbox = ttk.Spinbox(self, from_=0.0, to=10.0, increment=0.1, textvariable=self.maln_delay_var)
        self.maln_delay_spinbox.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

        # Auto Reply
        self.auto_reply_label = ttk.Label(self, text="Auto Reply:")
        self.auto_reply_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.auto_reply_options = ["On", "Off"]
        self.auto_reply_var = tk.StringVar(value=self.auto_reply_options[0])
        self.auto_reply_dropdown = ttk.Combobox(self, textvariable=self.auto_reply_var, values=self.auto_reply_options, state='readonly')
        self.auto_reply_dropdown.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

        # Emergency Stop
        self.emergency_stop_button = ttk.Button(self, text="Emergency Stop", command=self.emergency_stop)
        self.emergency_stop_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

        # Configure grid
        self.columnconfigure(1, weight=1)

    def emergency_stop(self):
        print("Emergency stop triggered")
        # Implement emergency stop logic here

if __name__ == "__main__":
    app = MacroConfig()
    app.mainloop()
