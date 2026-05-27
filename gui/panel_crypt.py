import tkinter as tk
from tkinter import messagebox
from core.cryptography import decrypt_msg, encrypt_msg


class PanelCryptography(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.frame_key = tk.LabelFrame(
            self, text="Key Definition", font=("Ubuntu Mono", 9, "bold")
        )
        self.frame_key.pack(pady=10, padx=10, fill="x")
        self.key = tk.Entry(self.frame_key, width=50)
        self.key.pack(pady=5)

        self.frame_encryption = tk.LabelFrame(
            self, text="Encryption", font=("Ubuntu Mono", 9, "bold")
        )
        self.frame_encryption.pack(pady=10, padx=10, fill="x")
        self.lbl = tk.Label(self.frame_encryption, text="Text to encrypt:")
        self.lbl.pack(pady=5)

        self.entry_en = tk.Entry(self.frame_encryption, width=50)
        self.entry_en.pack(pady=5)

        self.btn = tk.Button(
            self.frame_encryption, text="Encrypt", command=self.process_encryption
        )
        self.btn.pack(pady=5)

        self.lbl_result_1 = tk.Label(self.frame_encryption, text="Encrypted text")
        self.lbl_result_1.pack(pady=2)
        self.result_encrypt = tk.Entry(
            self.frame_encryption, width=65, state="readonly"
        )
        self.result_encrypt.pack(pady=5)

        self.frame_decryption = tk.LabelFrame(
            self, text="Decryption", font=("Ubuntu Mono", 9, "bold")
        )
        self.frame_decryption.pack(pady=10, padx=10, fill="x")
        self.lbl = tk.Label(self.frame_decryption, text="Text to decrypt:")
        self.lbl.pack(pady=5)

        self.entry_de = tk.Entry(self.frame_decryption, width=50)
        self.entry_de.pack(pady=5)

        self.btn = tk.Button(
            self.frame_decryption, text="Decrypt", command=self.process_decryption
        )
        self.btn.pack(pady=5)

        self.lbl_result_2 = tk.Label(self.frame_decryption, text="Decrypted text")
        self.lbl_result_2.pack(pady=2)
        self.result_decrypt = tk.Entry(
            self.frame_decryption, width=65, state="readonly"
        )
        self.result_decrypt.pack(pady=5)

    def process_encryption(self):
        key = self.key.get()
        msg = self.entry_en.get()
        try:
            encrypted_msg = encrypt_msg(msg, key)

            self.result_encrypt.config(state="normal")
            self.result_encrypt.delete(0, tk.END)
            self.result_encrypt.insert(0, encrypted_msg)
            self.result_encrypt.config(state="readonly")

        except ValueError as e:
            messagebox.showwarning("Error", str(e))

    def process_decryption(self):
        key = self.key.get()
        msg = self.entry_de.get()
        try:
            decrypted_msg = decrypt_msg(msg, key)

            self.result_decrypt.config(state="normal")
            self.result_decrypt.delete(0, tk.END)
            self.result_decrypt.insert(0, decrypted_msg)
            self.result_decrypt.config(state="readonly")

        except ValueError as e:
            messagebox.showwarning("Error", str(e))
