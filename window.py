import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets()
        self.label_file_path = None

    def create_widgets(self):
        verdmidalisti = ["Verdmidar", "VerdmidarLitlir", "A7", "A6", "A6L",
                        "A6B", "A5"]
        
        self.label = ttk.Label(text="Verðmerkja", style="BW.TLabel")
        self.label.grid(row=0, column=0)

        self.drop = ttk.Combobox(state="readonly", values=verdmidalisti)
        self.drop.set("Veldu verðmiðaútlit")
        self.drop.grid(row=1, column=0)
        
        self.hi_there = ttk.Button(text="Test", width=10, command=self.get_label_values)
        self.hi_there.grid(row=2, column=0)

        self.quit = ttk.Button(text="QUIT", width=10, command=root.destroy)
        self.quit.grid(row=3, column=0)

        self.input = ttk.Entry(width=50, state="normal")
        self.input.grid(row=3, column=3)

    def say_hi(self, box):
        print(box.get())

    def get_label_values(self):
        self.label_file_path = askopenfilename()

root = tk.Tk()
app = Application(master=root)
app.master.title("Verðmerking")
app.master.minsize(720, 480)
app.master.maxsize(720, 480)
app.mainloop()
