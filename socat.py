import tkinter as tk
from tkinter import messagebox, scrolledtext
import subprocess
import threading


class SocatGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Socat Virtual Serial Port Manager")

        # Command button
        self.run_button = tk.Button(root, text="Run Socat", command=self.run_socat)
        self.run_button.pack(pady=10)

        # Status display
        self.status_label = tk.Label(root, text="Status: Not running", fg="red")
        self.status_label.pack(pady=5)

        # Log display
        self.log = scrolledtext.ScrolledText(root, width=80, height=20)
        self.log.pack(pady=10)

        # Stop button
        self.stop_button = tk.Button(root, text="Stop Socat", command=self.stop_socat, state=tk.DISABLED)
        self.stop_button.pack(pady=10)

        self.socat_process = None

    def run_socat(self):
        self.run_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.status_label.config(text="Status: Running", fg="green")

        # Run socat in a separate thread
        self.socat_thread = threading.Thread(target=self.start_socat)
        self.socat_thread.start()

    def start_socat(self):
        cmd = ['socat', '-d', '-d', 'pty,raw,echo=0', 'pty,raw,echo=0']
        self.socat_process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        for line in self.socat_process.stdout:
            self.log.insert(tk.END, line)
            self.log.see(tk.END)

        self.socat_process.wait()
        self.status_label.config(text="Status: Not running", fg="red")
        self.run_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def stop_socat(self):
        if self.socat_process:
            self.socat_process.terminate()
            self.socat_process = None
            self.status_label.config(text="Status: Stopping...", fg="orange")
            self.run_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    app = SocatGUI(root)
    root.mainloop()
