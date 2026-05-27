import tkinter as tk
from tkinter import ttk

from gui.panel_hash import PanelHashing
from gui.panel_crypt import PanelCryptography
from gui.panel_sign import PanelSigning


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Basic Cryptography App")

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)

        self.init_panels()

    def init_panels(self):
        self.tab_hasing = PanelHashing(self.notebook)
        self.notebook.add(self.tab_hasing, text="Hashing")

        self.tab_crypto = PanelCryptography(self.notebook)
        self.notebook.add(self.tab_crypto, text="Cryptography")

        self.tab_signing = PanelSigning(self.notebook)
        self.notebook.add(self.tab_signing, text="Digital Signature")
