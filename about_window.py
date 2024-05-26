import tkinter as tk
from tkinter import ttk


class AboutWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("About")

        about_text = (
            "This is a dummy About window.\n\n"
            "Application Name: Example App\n"
            "Version: 1.0\n"
            "Author: Your Name\n"
        )

        self.label = ttk.Label(self, text=about_text, justify='center')
        self.label.pack(padx=20, pady=20)
