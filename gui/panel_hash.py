import tkinter as tk
from tkinter import messagebox
from core.hashing import gen_sha256


class PanelHashing(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.lbl = tk.Label(self, text="String to hash:")
        self.lbl.pack(pady=5)

        self.entry = tk.Entry(self, width=50)
        self.entry.pack(pady=5)

        self.btn = tk.Button(self, text="Generate Hash", command=self.process_hash)
        self.btn.pack(pady=5)

        self.result = tk.Entry(self, width=65, state="readonly")
        self.result.pack(pady=5)

    def process_hash(self):
        msg = self.entry.get()
        try:
            final_hash = gen_sha256(msg)

            self.result.config(state="normal")
            self.result.delete(0, tk.END)
            self.result.insert(0, final_hash)
            self.result.config(state="readonly")
        except ValueError as e:
            messagebox.showwarning("Error", str(e))
