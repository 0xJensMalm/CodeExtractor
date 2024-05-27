import os
import tkinter as tk
from tkinter import filedialog, scrolledtext

class CodeExporterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Code Exporter")

        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        self.select_folder_btn = tk.Button(self.frame, text="Select Folder", command=self.select_folder)
        self.select_folder_btn.pack(pady=5)

        self.run_script_btn = tk.Button(self.frame, text="Run Script", command=self.run_script)
        self.run_script_btn.pack(pady=5)

        self.output_text = scrolledtext.ScrolledText(self.frame, width=80, height=20, wrap=tk.WORD)
        self.output_text.pack(pady=10)

        self.folder_path = ""

    def select_folder(self):
        self.folder_path = filedialog.askdirectory()
        if self.folder_path:
            self.output_text.insert(tk.END, f"Selected Folder: {self.folder_path}\n\n")

    def run_script(self):
        if not self.folder_path:
            self.output_text.insert(tk.END, "Please select a folder first.\n\n")
            return

        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, f"Selected Folder: {self.folder_path}\n\n")

        excluded_files = {"config", "HEAD", "description"}

        for root, dirs, files in os.walk(self.folder_path):
            for file in files:
                if file in excluded_files:
                    continue
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    code = f.read()
                self.output_text.insert(tk.END, f"{file}:\n\n{code}\n\n")

        self.output_text.insert(tk.END, "\n--- End of Export ---\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = CodeExporterApp(root)
    root.mainloop()
