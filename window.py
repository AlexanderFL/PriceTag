import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.font_size = 14
        self.font = "Roboto"
        button_style = ttk.Style()
        button_style.configure("button.TButton", font=(self.font, self.font_size))

        self.create_widgets()

        self.label_file_path = None

    def create_widgets(self):
        verdmidautlit = ["Verdmidar", "VerdmidarLitlir", "A7", "A6", "A6L",
                         "A6B", "A5"]
        # Row 0
        self.title = ttk.Label(text="Verðmiðar", font=("Roboto", 20))
        self.title.place(x=720/2, y=25, anchor="center")

        # Row 1
        self.label = ttk.Label(text="Veldu verðmiðaútlit: ", style="BW.TLabel", font=(self.font, self.font_size))
        self.label.place(x=25, y=50)

        self.drop = ttk.Combobox(state="readonly", values=verdmidautlit, font=(self.font, self.font_size))
        self.drop.set("Verdmidar")
        self.drop.place(x=210, y=50)

        self.print_button = ttk.Button(text="Prenta", style="button.TButton")
        self.print_button.place(x=465, y=48)

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
