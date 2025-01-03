import tkinter as tk
from tkinter import ttk

class pdfEntry(tk.Frame):
    def __init__(self, parent, file_name, update_list_callback, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.fileName = file_name
        self.updateListCallback = update_list_callback
        self.create_widgets()
    
    def create_widgets(self):
        self.textLabel = ttk.Label(self, text=self.fileName, anchor="w", width=80)
        if len(self.fileName) > 80:
            self.textLabel.config(text=self.fileName[:77] + "...") 
        self.textLabel.pack(side="left", fill="x", padx=5, pady=2)

        self.deleteButton = ttk.Button(self, text="Delete", command=self.delete)
        self.deleteButton.pack(side="right", padx=2)

        self.downButton = ttk.Button(self, text="Down", command=self.moveDown)
        self.downButton.pack(side="right", padx=2)

        self.upButton = ttk.Button(self, text="Up", command=self.moveUp)
        self.upButton.pack(side="right", padx=2)

        self.bind("<Enter>", self.onHover)
        self.bind("<Leave>", self.onLeaveHover)

    def moveUp(self):
        self.updateListCallback(self.fileName, direction="up")

    def moveDown(self):
        self.updateListCallback(self.fileName, direction="down")

    def delete(self):
        self.updateListCallback(self.fileName, direction="delete")

    def onHover(self, event):
        self.config(borderwidth=1, relief="solid")

    def onLeaveHover(self, event):
        self.config(borderwidth=0)