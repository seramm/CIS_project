import tkinter as tk
from tkinter import messagebox
from core.signing import calc_signature, verify_signature


class PanelSigning(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # =================
        # Alice
        # =================
        self.frame_alice = tk.LabelFrame(self, text="Sender")
        self.frame_alice.pack(side="left", pady=10, padx=10, fill="both", expand=True)
        self.lbl_alice = tk.Label(self.frame_alice, text="Message being sent")
        self.lbl_alice.pack(pady=5)
        self.entry_alice = tk.Entry(self.frame_alice, width=50)
        self.entry_alice.pack(pady=5)
        self.btn_alice = tk.Button(
            self.frame_alice,
            text="Calculate signature and send",
            command=self.process_message,
        )
        self.btn_alice.pack(pady=5)
        self.lbl_signature_alice = tk.Label(self.frame_alice, text="Message Signature")
        self.lbl_signature_alice.pack(pady=2)
        self.signature_alice = tk.Entry(self.frame_alice, width=65, state="readonly")
        self.signature_alice.pack(pady=5)

        # ===================
        # Malicious Attacker
        # ===================
        self.frame_malicious = tk.LabelFrame(self, text="Malicious Attacker")
        self.frame_malicious.pack(
            side="left", pady=10, padx=10, fill="both", expand=True
        )
        self.lbl_malicious = tk.Label(self.frame_malicious, text="Message intercepted")
        self.lbl_malicious.pack(pady=5)
        self.entry_malicious = tk.Entry(self.frame_malicious, width=50)
        self.entry_malicious.pack(pady=5)
        self.btn_malicious = tk.Button(
            self.frame_malicious,
            text="Free the message",
            command=self.process_intruder,
        )
        self.btn_malicious.pack(pady=5)

        # =================
        # Bob
        # =================
        self.frame_bob = tk.LabelFrame(self, text="Receiver")
        self.frame_bob.pack(side="right", pady=10, padx=10, fill="both", expand=True)
        self.lbl_signature_received = tk.Label(
            self.frame_bob, text="Received Signature"
        )
        self.lbl_signature_received.pack(pady=2)
        self.signature_received = tk.Entry(self.frame_bob, width=65, state="readonly")
        self.signature_received.pack(pady=5)
        self.lbl_bob = tk.Label(self.frame_bob, text="Message received")
        self.lbl_bob.pack(pady=5)
        self.entry_bob = tk.Entry(self.frame_bob, width=50, state="readonly")
        self.entry_bob.pack(pady=5)
        self.btn = tk.Button(
            self.frame_bob,
            text="Calculate signature and compare",
            command=self.process_bob,
        )
        self.btn.pack(pady=5)
        self.lbl_signature_bob = tk.Label(self.frame_bob, text="Message Signature")
        self.lbl_signature_bob.pack(pady=2)
        self.signature_bob = tk.Entry(self.frame_bob, width=65, state="readonly")
        self.signature_bob.pack(pady=5)

        self.lbl_verification_icon = tk.Label(self.frame_bob, text="✅")
        self.lbl_verification_icon.pack(pady=5)
        self.lbl_verification_text = tk.Label(
            self.frame_bob, text="Signature not validated", fg="black"
        )
        self.lbl_verification_text.pack(pady=2)

    def process_message(self):
        msg = self.entry_alice.get()
        try:
            signature = calc_signature(msg)

            self.signature_alice.config(state="normal")
            self.signature_alice.delete(0, tk.END)
            self.signature_alice.insert(0, signature)
            self.signature_alice.config(state="readonly")

            self.signature_received.config(state="normal")
            self.signature_received.delete(0, tk.END)
            self.signature_received.insert(0, signature)
            self.signature_received.config(state="readonly")

            self.entry_malicious.delete(0, tk.END)
            self.entry_malicious.insert(0, msg)
            self.entry_malicious.config(state="normal")

        except ValueError as e:
            messagebox.showwarning("Error", str(e))

    def process_intruder(self):
        msg_michael = self.entry_malicious.get()

        self.entry_bob.config(state="normal")
        self.entry_bob.delete(0, tk.END)
        self.entry_bob.insert(0, msg_michael)
        self.entry_bob.config(state="readonly")

    def process_bob(self):
        msg = self.entry_bob.get()
        signature_received = self.signature_received.get()

        try:
            signature = calc_signature(msg)
            validation = verify_signature(msg, signature_received)

            self.signature_bob.config(state="normal")
            self.signature_bob.delete(0, tk.END)
            self.signature_bob.insert(0, signature)
            self.signature_bob.config(state="readonly")

            if validation:
                self.lbl_verification_icon.config(text="✅", fg="green")
                self.lbl_verification_text.config(
                    text="Integrity of message secure", fg="green"
                )
            else:
                self.lbl_verification_icon.config(text="❌", fg="red")
                self.lbl_verification_text.config(
                    text="Integrity of message broken", fg="red"
                )

        except ValueError as e:
            messagebox.showwarning("Error", str(e))
