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

        self.frame_result = tk.LabelFrame(
            self, text="Calculated SHA256 hashes", font=("Ubuntu Mono", 9, "bold")
        )
        self.frame_result.pack(pady=10, padx=10, fill="x")

        self.lbl_result_1 = tk.Label(self.frame_result, text="1st SHA256 hash")
        self.lbl_result_1.pack(pady=2)
        self.result_1 = tk.Entry(self.frame_result, width=65, state="readonly")
        self.result_1.pack(pady=5)

        self.lbl_result_2 = tk.Label(self.frame_result, text="2nd SHA256 hash")
        self.lbl_result_2.pack(pady=2)
        self.result_2 = tk.Entry(self.frame_result, width=65, state="readonly")
        self.result_2.pack(pady=5)

    def process_hash(self):
        msg = self.entry.get()
        try:
            final_hash_1 = gen_sha256(msg)
            final_hash_2 = gen_sha256(msg)

            self.result_1.config(state="normal")
            self.result_1.delete(0, tk.END)
            self.result_1.insert(0, final_hash_1)
            self.result_1.config(state="readonly")

            self.result_2.config(state="normal")
            self.result_2.delete(0, tk.END)
            self.result_2.insert(0, final_hash_2)
            self.result_2.config(state="readonly")

        except ValueError as e:
            messagebox.showwarning("Error", str(e))
