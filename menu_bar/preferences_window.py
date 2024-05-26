import tkinter as tk
from tkinter import ttk, messagebox


class PreferencesWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Preferences")
        # Create checkboxes
        self.option1_var = tk.BooleanVar(value=True)
        self.option2_var = tk.BooleanVar(value=False)
        self.option3_var = tk.BooleanVar(value=True)
        self.option1_check = ttk.Checkbutton(self, text="Enable Option 1", variable=self.option1_var)
        self.option1_check.pack(anchor='w', padx=20, pady=5)
        self.option2_check = ttk.Checkbutton(self, text="Enable Option 2", variable=self.option2_var)
        self.option2_check.pack(anchor='w', padx=20, pady=5)
        self.option3_check = ttk.Checkbutton(self, text="Enable Option 3", variable=self.option3_var)
        self.option3_check.pack(anchor='w', padx=20, pady=5)
        # Save button
        self.save_button = ttk.Button(self, text="Save", command=self.save_preferences)
        self.save_button.pack(pady=10)

    def save_preferences(self):
        prefs = {
            "Option 1": self.option1_var.get(),
            "Option 2": self.option2_var.get(),
            "Option 3": self.option3_var.get(),
        }
        messagebox.showinfo("Preferences Saved", f"Preferences have been saved:\n{prefs}")


if __name__ == "__main__":
    root = tk.Tk()  # create a Tk root window
    app = PreferencesWindow(root)
    root.mainloop()
