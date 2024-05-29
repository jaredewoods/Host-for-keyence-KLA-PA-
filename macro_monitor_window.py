import tkinter as tk
from tkinter import ttk
import event_dispatcher


class MacroMonitorWindow(tk.Tk):
    def __init__(self, dispatcher1):
        super().__init__()

        self.dispatcher = dispatcher1
        self.title("Macro Monitor")

        self.custom_font = ('Arial', 18)

        self.style = ttk.Style()
        self.style.configure("Treeview.Heading", font=self.custom_font)
        self.style.configure("Treeview", rowheight=30, font=self.custom_font)

        self.sequence_status_table = ttk.Treeview(self, columns=("Description", "Status"), show='headings', style="Treeview", height=6)
        self.sequence_status_table.heading("Description", text="Description")
        self.sequence_status_table.heading("Status", text="Status")
        self.sequence_status_table.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        self.steps_data = [
            ("Sequence Initialized", "Inactive"),
            ("Move to ReadyPos", "Inactive"),
            ("Aligning Wafer", "Inactive"),
            ("Capturing Data", "Inactive"),
            ("Processing Data", "Inactive"),
            ("Sequence Completed", "Inactive")
        ]

        self.status_colors = {
            "Inactive": {"background": "", "foreground": "grey"},
            "Queued": {"background": "black", "foreground": "white"},
            "In Progress": {"background": "dark blue", "foreground": "white"},
            "Completed": {"background": "dark green", "foreground": "white"},
            "Alarm": {"background": "dark red", "foreground": "white"}
        }

        for step in self.steps_data:
            self.sequence_status_table.insert("", "end", values=(step[0], step[1]))

        self.apply_status_colors()

        # Cycle Information
        self.cycle_frame = ttk.LabelFrame(self, text="Cycles")
        self.cycle_frame.grid(row=1, column=0, padx=(5, 0), pady=(0, 10), sticky="")

        self.cycle_table = ttk.Treeview(self.cycle_frame, columns=("Parameter", "Value"), show='', height=2)
        self.cycle_table.column("Parameter", anchor="e", width=120)
        self.cycle_table.column("Value", anchor="w", width=50)
        self.cycle_table.grid(row=0, column=0, sticky="nsew")

        cycle_data = [
            ("Current:", "0"),
            ("Pending:", "0")
        ]

        for cycle in cycle_data:
            self.cycle_table.insert("", "end", values=cycle)

        # Offsets Display
        self.offsets_frame = ttk.LabelFrame(self, text="Offsets")
        self.offsets_frame.grid(row=1, column=1, padx=(5, 20), pady=(0, 10), sticky="")

        self.offsets_table = ttk.Treeview(self.offsets_frame, columns=("Parameter", "Value"), show='', height=2)
        self.offsets_table.column("Parameter", anchor="e", width=120)
        self.offsets_table.column("Value", anchor="w", width=50)
        self.offsets_table.grid(row=0, column=0, sticky="nsew")

        offsets_data = [
            ("0.00", ' deg'),
            ("0.00", ' mm'),
        ]

        for offset in offsets_data:
            self.offsets_table.insert("", "end", values=offset)

        # Emergency Stop Button
        self.emergency_stop_button = ttk.Button(self, text="Emergency Stop", command=self.handle_emergency_stop)
        self.emergency_stop_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Button to manually update total cycles for testing
        self.test_button = ttk.Button(self, text="Test Update Total Cycles", command=lambda: self.update_total_cycles(20))
        self.test_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Configuring grid
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)

        self.dispatcher.register_event("macro_update", self.update_status)
        self.dispatcher.register_event("cycle_update", self.update_cycle_info)
        self.dispatcher.register_event("offset_update", self.update_offsets)
        self.dispatcher.register_event("total_cycles_update", self.update_total_cycles)

    def apply_status_colors(self):
        for idx, step in enumerate(self.steps_data):
            status = step[1]
            item_id = self.sequence_status_table.get_children()[idx]
            colors = self.status_colors.get(status, {"background": "", "foreground": "grey"})
            self.sequence_status_table.tag_configure(status, background=colors["background"], foreground=colors["foreground"])
            self.sequence_status_table.item(item_id, tags=(status,))

    def handle_emergency_stop(self):
        self.dispatcher.emit("emergencyStop")

    def update_status(self, data):
        for idx, status in enumerate(data):
            item_id = self.sequence_status_table.get_children()[idx]
            self.sequence_status_table.item(item_id, values=(self.steps_data[idx][0], status))
            colors = self.status_colors.get(status, {"background": "", "foreground": "grey"})
            self.sequence_status_table.tag_configure(status, background=colors["background"], foreground=colors["foreground"])
            self.sequence_status_table.item(item_id, tags=(status,))

    def update_cycle_info(self, data):
        completed_cycles, total_cycles = data
        cycle_data = [
            ("Current:", str(completed_cycles)),
            ("Pending:", str(total_cycles - completed_cycles))
        ]
        for idx, cycle in enumerate(cycle_data):
            item_id = self.cycle_table.get_children()[idx]
            self.cycle_table.item(item_id, values=cycle)

    def update_offsets(self, data):
        positional_offset, angular_offset = data
        offsets_data = [
            (str(positional_offset), ' mm'),
            (str(angular_offset), ' deg')
        ]
        for idx, offset in enumerate(offsets_data):
            item_id = self.offsets_table.get_children()[idx]
            self.offsets_table.item(item_id, values=offset)

    def update_total_cycles(self, new_total):
        self.cycle_frame.config(text=f"Total Cycles: {new_total}")


if __name__ == "__main__":
    dispatcher = event_dispatcher.EventDispatcher()
    app = MacroMonitorWindow(dispatcher)
    app.mainloop()
