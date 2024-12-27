import tkinter as tk
from tkinter import ttk
from pdfEntry import pdfEntry

class ScrollableFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.chosenFilesList = tk.Canvas(self)

        self.chosenFilesScrollBar = ttk.Scrollbar(self.chosenFilesList, orient="vertical", command=self.chosenFilesList.yview)

        self.chosenFilesList.configure(yscrollcommand=self.chosenFilesScrollBar.set)

        self.scrollableFrame = ttk.Frame(self.chosenFilesList)
        self.scrollableWindow = self.chosenFilesList.create_window((0, 0), window=self.scrollableFrame, anchor="nw")

        self.chosenFilesScrollBar.pack(side="right", fill="y")
        self.chosenFilesList.pack(side="left", fill="both", expand=True)

        self.scrollableFrame.bind("<Configure>", self.onFrameConfigure)
        self.chosenFilesList.bind("<Configure>", self.onCanvasConfigure)
        self.chosenFilesList.bind("<MouseWheel>", self.onMouseWheel)
        self.scrollableFrame.bind("<MouseWheel>", self.onMouseWheel)


    def onFrameConfigure(self, event):
        self.chosenFilesList.configure(scrollregion=self.chosenFilesList.bbox("all"))

    def onCanvasConfigure(self, event):
        canvasWidth = event.width
        self.chosenFilesList.itemconfig(self.scrollableWindow, width=canvasWidth)

    def onMouseWheel(self, event):
        self.chosenFilesList.yview_scroll(-1*int(event.delta/120), "units")

    def update_scrollregion(self):
        self.chosenFilesList.configure(scrollregion=self.chosenFilesList.bbox("all"))