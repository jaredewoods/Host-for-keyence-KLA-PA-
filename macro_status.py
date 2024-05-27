import tkinter as tk
from tkinter import ttk
"""**Summary of Current State and Next Steps**

**Objective:**
The goal is to bring the `ProgramStatusWindow` UI to life by integrating it with the macro service in your application. The UI will display the sequence status, cycle information, and offsets, updating dynamically based on the macro sequence execution.

**Current State:**
1. **UI Design:**
   - The `ProgramStatusWindow` is designed with three main sections: Sequence Status (steps table), Cycles, and Offsets.
   - Steps table uses tags to color-code statuses: Completed (green), In Progress (blue), Alarm (red), Queued (default).
   - Cycles and Offsets tables are set up but not yet dynamically updated.

2. **Macro Sequence Integration:**
   - You have outlined the flow of macro events and how they should update the steps table:
     - **Macro Starts:** "Sequence Started" (Completed), "Move to ReadyPos" (In Progress), others (Queued).
     - **snd_command_maln:** "Move to ReadyPos" (Completed), "Aligning Wafer" (In Progress).
     - **wait_3_secs:** "Aligning Wafer" (Completed), "Pausing for DAQ" (In Progress).
     - **send_command_t1:** "Pausing for DAQ" (Completed), "Capturing Data" (In Progress).
     - **increment_cycle:** "Capturing Data" (Completed), update cycle counts, reset sequence if not complete.

3. **Event Handling:**
   - Existing dispatcher will be used to handle and emit events.
   - Need to register new event handlers for updating the steps table, cycle counts, and offsets.

**Next Steps:**
1. **Define Event Handlers:**
   - Create event handlers for each macro event that will update the respective sections of the UI.
   - Example handlers:
     - `handle_macro_start`
     - `handle_snd_command_maln`
     - `handle_wait_3_secs`
     - `handle_send_command_t1`
     - `handle_increment_cycle`

2. **Register Event Handlers:**
   - Register these handlers with the dispatcher to ensure they are called at the appropriate times during the macro sequence.

3. **Update UI:**
   - Implement the logic within each event handler to update the UI components (steps table, cycle counts, offsets).
   - Ensure thread safety by synchronizing UI updates if they are triggered from different threads.

4. **Test Integration:**
   - Verify that the steps table, cycle counts, and offsets update correctly in response to the macro sequence events.
   - Test for any edge cases or errors in the sequence flow to ensure robustness.

By following these steps, you will be able to bring the `ProgramStatusWindow` to life, providing real-time updates on the macro sequence status, cycles, and offsets. This will enhance the usability and functionality of your application."""

class ProgramStatusWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Program Execution Status")

        # Steps and Status Table
        self.steps_frame = ttk.LabelFrame(self, text="Sequence Status")
        self.steps_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        self.steps_table = ttk.Treeview(self.steps_frame, columns=("Step", "Description", "Status"), show='headings', height=6)
        self.steps_table.heading("Step", text="Step")
        self.steps_table.column("Step", width=40, anchor="center")
        self.steps_table.heading("Description", text="Description")
        self.steps_table.column("Description", width=130, anchor="w")
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
            (4, "Pausing for DAQ", "Queued"),
            (5, "Capturing Data", "Queued"),
            (6, "Sequence Complete", "Queued")
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
