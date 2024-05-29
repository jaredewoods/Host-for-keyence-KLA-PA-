# macro_monitor_window.py

import tkinter as tk
from tkinter import ttk
import event_dispatcher


class MacroMonitorWindow(tk.Tk):
    def __init__(self, dispatcher1):
        super().__init__()

        self.offsets_frame = None
        self.offsets_table = None
        self.cycle_table = None
        self.cycle_frame = None
        self.status_colors = None
        self.steps_data = None
        self.sequence_status_table = None
        self.dispatcher = dispatcher1
        self.title("Macro Monitor")

        self.custom_font = ('Arial', 12)

        self.style = ttk.Style()
        self.style.configure("Treeview.Heading", font=self.custom_font)
        self.style.configure("Treeview", rowheight=30, font=self.custom_font)

        # Calls the separated table creation functions
        self.create_sequence_status_table()
        self.create_cycle_table()
        self.create_offsets_table()

        # Emergency Stop Button
        self.emergency_stop_button = ttk.Button(self, text="Emergency Stop", command=self.handle_emergency_stop)
        self.emergency_stop_button.grid(row=2, column=0, columnspan=2, pady=10, padx=5, sticky='ew')

        # Configuring grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)

        # Dispatcher register events
        self.dispatcher.register_event("macro_update", self.update_status)
        self.dispatcher.register_event("cycle_update", self.update_cycle_info)
        self.dispatcher.register_event("offset_update", self.update_offsets)
        self.dispatcher.register_event("total_cycles_update", self.update_total_cycles)

    def create_sequence_status_table(self):
        self.sequence_status_table = ttk.Treeview(self, columns=("Description", "Status"), show='headings', style="Treeview", height=6)
        self.sequence_status_table.column("Description", width=140, anchor="center")  # adjust as needed
        self.sequence_status_table.column("Status", width=80, anchor="center")  # adjust as needed
        self.sequence_status_table.heading("Description", text="Description")
        self.sequence_status_table.heading("Status", text="Status")
        self.sequence_status_table.grid(row=0, column=0, columnspan=2, padx=10, pady=(10, 5), sticky="nsew")

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

    def create_cycle_table(self):
        self.cycle_frame = ttk.LabelFrame(self, text='Cycle')
        self.cycle_frame.grid(row=1, column=0, padx=(10, 5), pady=5)

        self.cycle_table = ttk.Treeview(self.cycle_frame, columns=("Parameter", "Value"), show='', height=2)
        self.cycle_table.column("Parameter", anchor="e", width=90)
        self.cycle_table.column("Value", anchor="w", width=30)
        self.cycle_table.grid(row=0, column=0)

        cycle_data = [
            ("Current:", "0"),
            ("Remaining:", "0")
        ]

        for cycle in cycle_data:
            self.cycle_table.insert("", "end", values=cycle)

    def create_offsets_table(self):
        self.offsets_frame = ttk.LabelFrame(self, text='Offsets')
        self.offsets_frame.grid(row=1, column=1, padx=(0, 10), pady=5)

        self.offsets_table = ttk.Treeview(self.offsets_frame, columns=("Parameter", "Value"), show='', height=2)
        self.offsets_table.column("Parameter", anchor="e", width=60)
        self.offsets_table.column("Value", anchor="w", width=40)
        self.offsets_table.grid(row=0, column=0, sticky="nsew")

        offsets_data = [
            ("0.00", ' deg'),
            ("0.00", ' mm'),
        ]

        for offset in offsets_data:
            self.offsets_table.insert("", "end", values=offset)

        # Emergency Stop Button
        self.emergency_stop_button = ttk.Button(self, text="Emergency Stop", command=self.handle_emergency_stop)
        self.emergency_stop_button.grid(row=2, column=0, columnspan=2, pady=10, padx=5, sticky='ew')

        # Configuring grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
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
