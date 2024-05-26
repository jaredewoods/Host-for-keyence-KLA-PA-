import tkinter as tk
from tkinter import ttk


class ProgramStatusWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Program Execution Status")

        # Steps and Status Table
        self.steps_frame = ttk.LabelFrame(self, text="Sequence Status")
        self.steps_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        self.steps_table = ttk.Treeview(self.steps_frame, columns=("Step", "Description", "Status"), show='headings', height=4)
        self.steps_table.heading("Step", text="Step")
        self.steps_table.column("Step", width=40, anchor="center")
        self.steps_table.heading("Description", text="Description")
        self.steps_table.column("Description", width=120, anchor="w")
        self.steps_table.heading("Status", text="Status")
        self.steps_table.column("Status", width=80, anchor="center")
        self.steps_table.grid(row=0, column=0, sticky="nsew")

        # Configure tags for row colors
        self.steps_table.tag_configure('completed', background='green')
        self.steps_table.tag_configure('in_progress', background='blue')
        self.steps_table.tag_configure('alarm', background='red')
        self.steps_table.tag_configure('queued', background='')

        steps_data = [
            (1, "Sequence Started", "Alarm"),
            (2, "Move to ReadyPos", "Completed"),
            (3, "Aligning Wafer", "In Progress"),
            (4, "Capturing Data", "Queued")
        ]

        for step in steps_data:
            tag = 'queued'
            if step[2] == "Completed":
                tag = 'completed'
            elif step[2] == "In Progress":
                tag = 'in_progress'
            elif step[2] == "Alarm":
                tag = 'alarm'
            self.steps_table.insert("", "end", values=step, tags=(tag,))

        # Cycle Information
        self.cycle_frame = ttk.LabelFrame(self, text="Cycles")
        self.cycle_frame.grid(row=1, column=0, padx=(5, 0), pady=(0, 10), sticky="")

        self.cycle_table = ttk.Treeview(self.cycle_frame, columns=("Parameter", "Value"), show='', height=2)
        self.cycle_table.column("Parameter", width=60, anchor="e")
        self.cycle_table.column("Value", width=26, anchor="w")
        self.cycle_table.grid(row=0, column=0, sticky="")

        cycle_data = [
            ("Current:", "5"),
            ("Pending:", "15")
        ]

        # Configure tags for cycle table
        self.cycle_table.tag_configure('cycle_bg', background='')

        for cycle in cycle_data:
            self.cycle_table.insert("", "end", values=cycle, tags=('cycle_bg',))

        # Offsets Display
        self.offsets_frame = ttk.LabelFrame(self, text="Offsets")
        self.offsets_frame.grid(row=1, column=1, padx=(5, 20), pady=(0, 10), sticky="")

        self.offsets_table = ttk.Treeview(self.offsets_frame, columns=("Parameter", "Value"), show='', height=2)
        self.offsets_table.column("Parameter", width=60, anchor="e")
        self.offsets_table.column("Value", width=40, anchor="w")
        self.offsets_table.grid(row=0, column=0, sticky="")

        offsets_data = [
            ("-127.26", ' deg'),
            ("0.05", ' mm'),
                    ]

        # Configure tags for offsets table
        self.offsets_table.tag_configure('offset_bg', background='')

        for offset in offsets_data:
            self.offsets_table.insert("", "end", values=offset, tags=('offset_bg',))

        # Configuring grid
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)


if __name__ == "__main__":
    app = ProgramStatusWindow()
    app.mainloop()
