from pdfMerger import mergePdf
import tkinter as tk
from tkinter import ttk
import tkinter.filedialog as fd
from scrollableAreaClass import ScrollableFrame
from pdfEntry import pdfEntry

class mergerWindow:
    def __init__(self, title="PDF Merger", width=400, height=300):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")
        self.create_widgets()

    def create_widgets(self):
        self.label = ttk.Label(self.root, text="Welcome to PDF Merger!")
        self.label.pack(pady=20)

        self.button = ttk.Button(self.root, text="Choose PDF files.", command=self.on_button_click)
        self.button.pack(pady=10)

        self.chosenFilesFrame = ttk.Frame(self.root)
        self.chosenFilesFrame.pack(pady=10, padx=10, fill="both", expand=True)

        self.chosenFilesLabel = ttk.Label(self.chosenFilesFrame, text="Chosen files:")
        self.chosenFilesLabel.pack(pady=5, anchor="w")

        self.scrollableArea = ScrollableFrame(self.chosenFilesFrame, borderwidth=5, relief="groove")
        self.scrollableArea.pack(fill="both", expand=True)

        self.errorMessage = ttk.Label(self.root, text="", foreground="red")
        self.errorMessage.pack(pady=5)

        self.mergeButton = ttk.Button(self.root, text="Merge PDF's", command=self.onMergePressed)
        self.mergeButton.pack(pady=10)


    def onMergePressed(self):
        if hasattr(self, 'selectedFiles') and self.selectedFiles:
            outputFile = fd.asksaveasfilename(
                title="Choose a name for the merged PDF",
                filetypes=[("PDF Files", "*.pdf")]
            )

            if outputFile and not outputFile.endswith(".pdf"):
                outputFile += ".pdf"

            if outputFile:
                mergePdf(self.selectedFiles, outputFile)
                for widget in self.scrollableArea.scrollableFrame.winfo_children():
                    widget.destroy()
                self.selectedFiles = []
                self.errorMessage.config(text="Merged successfully!", foreground="green")
            else:
                self.errorMessage.config(text="Please choose a valid name for the output file")
        else:
            self.errorMessage.config(text="Please choose a few files first")

    def on_button_click(self):
        self.errorMessage.config(text="")

        files = fd.askopenfilenames(
            title="Choose PDF Files",
            filetypes=[("PDF Files", "*.pdf")]
        )

        if files:
            self.selectedFiles = [file for file in files]
            self.updateFileList()


    def updateFileList(self):
        for widget in self.scrollableArea.scrollableFrame.winfo_children():
            if isinstance(widget, pdfEntry):
                widget.destroy()

        for file in self.selectedFiles:
            label = pdfEntry(self.scrollableArea.scrollableFrame, file, self.update_list_callback)
            label.bind("<MouseWheel>", self.scrollableArea.onMouseWheel)
            for widget in label.winfo_children():
                widget.bind("<MouseWheel>", self.scrollableArea.onMouseWheel)
            label.anchor("w")
            label.pack(fill="x", padx=5, pady=2)

        self.scrollableArea.update_scrollregion()

    def update_list_callback(self, file_name, direction):
        if hasattr(self, 'selectedFiles'):
            index = self.selectedFiles.index(file_name)

            if index > 0 and direction == "up" and len(self.selectedFiles) > 1:
                self.selectedFiles[index], self.selectedFiles[index-1] = self.selectedFiles[index-1], self.selectedFiles[index]
            elif index < len(self.selectedFiles)-1 and direction == "down" and len(self.selectedFiles) > 1:
                self.selectedFiles[index], self.selectedFiles[index+1] = self.selectedFiles[index+1], self.selectedFiles[index]
            elif direction == "delete":
                self.selectedFiles.remove(file_name)
        
        self.updateFileList()
 
    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = mergerWindow(title="PDF Merger", width=800, height=600)
    app.run()