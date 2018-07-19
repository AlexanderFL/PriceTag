import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from cleanup import LabelApp


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.font_size = 14
        self.font = "Roboto"
        self.label_file_path = None
        
        button_style = ttk.Style()
        button_style.configure("button.TButton", font=(self.font, self.font_size))

        self.create_widgets()

    def create_widgets(self):
        verdmidautlit = ["Verdmidar", "VerdmidarLitlir", "A7", "A6", "A6L",
                         "A6B", "A5"]
        # Row 0 - Main title
        self.title = ttk.Label(text="Verðmiðar", font=("Roboto", 20))
        self.title.place(x=720/2, y=25, anchor="center")

        # Row 1 - Main Interface 1
        get_file_path = None
        self.button_select = ttk.Button(text="Veldu textaskranna með verðnúmerunum", style="button.TButton", command=self.ask_for_file)
        self.button_select.place(x=25, y=50)

        self.file_selected_box = ttk.Entry(state="readonly", font=(self.font, self.font_size))
        self.file_selected_box.place(x=390, y=52)
        
        # Row 2 - Main Interface 2
        self.label = ttk.Label(text="Veldu verðmiðaútlit: ", style="BW.TLabel", font=(self.font, self.font_size))
        self.label.place(x=25, y=90)

        self.drop = ttk.Combobox(state="readonly", values=verdmidautlit, font=(self.font, self.font_size))
        self.drop.set("Verdmidar")
        self.drop.place(x=210, y=90)

        self.print_button = ttk.Button(text="Prenta", style="button.TButton", command=self.print_labels)
        self.print_button.place(x=465, y=87)

        # Row 3 - Separator
        self.sep = ttk.Separator(orient="horizontal")
        self.sep.place(x=0, y=140, relwidth=5)

        # Row 4 - Settings title
        self.settings_title = ttk.Label(text="Stillingar", font=("Roboto", 20))
        self.settings_title.place(x=720/2, y=170, anchor="center")

        # Row 5 - Settings
        self.fake_print_settings = ttk.Checkbutton(text="Fake print")
        self.fake_print_settings.place(x=50, y=200)
        

    def ask_for_file(self):
        self.label_file_path = askopenfilename()
        normalize_path = self.label_file_path.split("/")
        normalize_path = normalize_path[len(normalize_path) - 1]
        self.file_selected_box.config(state="normal")
        self.file_selected_box.delete(0, 'end')
        self.file_selected_box.insert(0, normalize_path)
        self.file_selected_box.config(state="readonly")

    def print_labels(self):
        print(self.fake_print_settings.state()[0])
        main_file = "C:\\Users\\ht-afgr7\\Desktop\\PriceTag-master\\PriceTag-master\\test1.xlsm"
        label_file = self.label_file_path
        label_type = self.drop.get()
        #self.la = LabelApp(main_file, label_file, label_type)
        #self.la.is_fake_print = True
        #self.la.start_working()
        #self.la.close_application(False)


root = tk.Tk()
app = Application(master=root)
app.master.title("Verðmerking")
app.master.minsize(720, 480)
app.master.maxsize(720, 480)
app.mainloop()
