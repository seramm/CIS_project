from copy import deepcopy
import tkinter as tk
from core.blockchain import Block, Blockchain


class PanelBlockchain(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.bc_original = Blockchain()
        self.bc_malicious = deepcopy(self.bc_original)

        tk.Label(
            self,
            text="Blockchain",
            font=("Arial", 20, "bold"),
        ).pack(pady=10)

        frame_management = tk.LabelFrame(
            self, text="Blockchain management", padx=10, pady=10
        )
        frame_management.pack(fill="x", padx=15, pady=5)

        tk.Label(frame_management, text="Data:").pack(side="left", padx=5)
        self.entry_data = tk.Entry(frame_management, width=45)
        self.entry_data.pack(side="left", padx=10, fill="x", expand=True)

        btn_add = tk.Button(
            frame_management,
            text="Add to the blockchain",
            command=self.add_block,
        )
        btn_add.pack(side="left", padx=5)

        self.lbl_status_text = tk.Label(
            frame_management,
            text="BLOCKCHAIN INTEGRITY - OK",
            fg="green",
        )
        self.lbl_status_text.pack(side="right", padx=5)
        btn_refresh = tk.Button(
            frame_management,
            text="Refresh hashes",
            command=self.render_blockchain_malicious,
        )
        btn_refresh.pack(side="left", padx=5)

        canvas_container_trustfull = tk.Frame(self)
        canvas_container_trustfull.pack(
            side="left", fill="both", expand=True, padx=15, pady=10
        )

        self.canvas_trustfull = tk.Canvas(
            canvas_container_trustfull, highlightthickness=0
        )
        scrollbar = tk.Scrollbar(
            canvas_container_trustfull,
            orient="vertical",
            command=self.canvas_trustfull.yview,
        )

        self.frame_block_render_trustfull = tk.Frame(self.canvas_trustfull)
        self.frame_block_render_trustfull.bind(
            "<Configure>",
            lambda e: self.canvas_trustfull.configure(
                scrollregion=self.canvas_trustfull.bbox("all")
            ),
        )

        self.canvas_trustfull.create_window(
            (0, 0), window=self.frame_block_render_trustfull, anchor="nw"
        )
        self.canvas_trustfull.configure(yscrollcommand=scrollbar.set)

        self.canvas_trustfull.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        canvas_container_malicious = tk.Frame(self)
        canvas_container_malicious.pack(
            side="right", fill="both", expand=True, padx=15, pady=10
        )

        self.canvas_malicious = tk.Canvas(
            canvas_container_malicious, highlightthickness=0
        )
        scrollbar = tk.Scrollbar(
            canvas_container_malicious,
            orient="vertical",
            command=self.canvas_malicious.yview,
        )

        self.frame_block_render_malicious = tk.Frame(self.canvas_malicious)
        self.frame_block_render_malicious.bind(
            "<Configure>",
            lambda e: self.canvas_malicious.configure(
                scrollregion=self.canvas_malicious.bbox("all")
            ),
        )

        self.canvas_malicious.create_window(
            (0, 0), window=self.frame_block_render_malicious, anchor="nw"
        )
        self.canvas_malicious.configure(yscrollcommand=scrollbar.set)

        self.canvas_malicious.pack(side="right", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        self.render_blockchain_trustfull()
        self.render_blockchain_malicious()

    def render_blockchain_trustfull(self):
        for widget in self.frame_block_render_trustfull.winfo_children():
            widget.destroy()

        blockchain_integrity = self.bc_original.validate_integrity()

        for i, block in enumerate(self.bc_original.chain):

            box = tk.LabelFrame(
                self.frame_block_render_trustfull,
                text=f" BLOCK #{block.index} ",
                padx=10,
                pady=8,
                bd=2,
                relief="solid",
            )
            box.pack(pady=8, padx=15, fill="x")

            tk.Label(box, text="Data:").grid(row=0, column=0, sticky="w")
            entry_data = tk.Entry(box, width=55)
            entry_data.grid(row=0, column=1, padx=10, pady=2, sticky="w")
            entry_data.insert(0, block.data)
            entry_data.config(state="readonly")

            entry_data.bind(
                "<KeyRelease>",
                lambda event, idx=i, ent=entry_data: self.action_modify_data(idx, ent),
            )

            tk.Label(
                box,
                text="Prev Hash:",
            ).grid(row=1, column=0, sticky="w")
            tk.Label(
                box,
                text=block.previous_hash,
            ).grid(row=1, column=1, padx=10, sticky="w")

            tk.Label(
                box,
                text="Current Hash:",
            ).grid(row=2, column=0, sticky="w")
            tk.Label(
                box,
                text=block.hash,
            ).grid(row=2, column=1, padx=10, sticky="w")

        if blockchain_integrity:
            self.lbl_status_text.config(text="BLOCKCHAIN INTEGRITY - OK", fg="green")
        else:
            self.lbl_status_text.config(
                text="BLOCKCHAIN INTEGRITY - COMPROMISED", fg="red"
            )

    def render_blockchain_malicious(self):
        for widget in self.frame_block_render_malicious.winfo_children():
            widget.destroy()

        blockchain_integrity = self.bc_malicious.validate_integrity()

        for i, block in enumerate(self.bc_malicious.chain):

            box = tk.LabelFrame(
                self.frame_block_render_malicious,
                text=f" BLOCK #{block.index} ",
                padx=10,
                pady=8,
                bd=2,
                relief="solid",
            )
            box.pack(pady=8, padx=15, fill="x")

            tk.Label(box, text="Data:").grid(row=0, column=0, sticky="w")
            entry_data = tk.Entry(box, width=55)
            entry_data.grid(row=0, column=1, padx=10, pady=2, sticky="w")
            entry_data.insert(0, block.data)

            entry_data.bind(
                "<KeyRelease>",
                lambda event, idx=i, ent=entry_data: self.action_modify_data(idx, ent),
            )

            tk.Label(
                box,
                text="Prev Hash:",
            ).grid(row=1, column=0, sticky="w")
            tk.Label(
                box,
                text=block.previous_hash,
            ).grid(row=1, column=1, padx=10, sticky="w")

            tk.Label(
                box,
                text="Current Hash:",
            ).grid(row=2, column=0, sticky="w")
            tk.Label(
                box,
                text=block.hash,
            ).grid(row=2, column=1, padx=10, sticky="w")

        if blockchain_integrity:
            self.lbl_status_text.config(text="BLOCKCHAIN INTEGRITY - OK", fg="green")
        else:
            self.lbl_status_text.config(
                text="BLOCKCHAIN INTEGRITY - COMPROMISED", fg="red"
            )

    def add_block(self):
        data = self.entry_data.get()
        if not data:
            return

        previous_block = self.bc_original.chain[-1]
        new_block = Block(len(self.bc_original.chain), data, previous_block.hash)

        self.bc_original.add_block_raw(deepcopy(new_block))
        self.bc_malicious.add_block_raw(deepcopy(new_block))

        self.render_blockchain_trustfull()
        self.render_blockchain_malicious()

        self.entry_data.delete(0, tk.END)

    def action_modify_data(self, index, entry_object):
        modified_test = entry_object.get()

        self.bc_malicious.chain[index].data = modified_test
        self.bc_malicious.recalculate_hashes()

    def refresh_malicious(self):
        self.render_blockchain_malicious()
