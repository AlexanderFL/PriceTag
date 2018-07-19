import win32com.client as win32
from time import sleep

class LabelApp:
    def __init__(self, excel_file_path, label_file_path, label_type,
                 interactive=True, visible=True, display_alerts=True):
        # Debug variables
        self.is_fake_print = False

        # Variables
        self.excel_file_path = excel_file_path
        self.label_file_path = label_file_path
        self.label_type = label_type

        self.excel_file_name = excel_file_path.split("\\")
        self.excel_file_name = self.excel_file_name[len(self.excel_file_name) - 1]

        # Open Excel
        self.xl = win32.gencache.EnsureDispatch("Excel.Application")
        self.xl.Interactive = interactive
        self.xl.Visible = visible
        self.xl.DisplayAlerts = display_alerts

        # Open the Excel file and set the sheet to front
        self.xlBook = self.xl.Workbooks.Open(self.excel_file_path)
        self.xlSheet = self.xlBook.Worksheets('Front')

        # Setting the label type
        self.xlSheet.Cells(12, 13).Value = self.label_type
        # Getting the number of labels per page
        self.nr_of_labels = int(self.xlSheet.Cells(12, 14).Value)

        # label_nrs[] contains all of the label numbers ex. WHI-FSCR80421
        self.label_nrs = []
        with open(self.label_file_path) as f:
            self.label_nrs = f.read().splitlines()
        
    def print_page(self):
        if not self.is_fake_print:
            self.run_command("Prenta")
        else:
            print("Printing...")

    def run_command(self, command):
        self.xlBook.Application.Run(self.excel_file_name + "!" + command)

    def erase_label_column(self, stop=14):
        for x in range(2, stop):
            self.xlSheet.Cells(x, 1).Value = None

    def close_application(self, save=True):
        self.xlBook.Close(save)
        self.xl.Quit()

    def refresh_query(self):
        self.run_command("RefreshQuery")
    
    def start_working(self):
        label_count = 0
        label_sub_count = 0

        while label_count != len(self.label_nrs):
            if label_sub_count % self.nr_of_labels == 0 and label_count is not 0:
                label_sub_count = 0
                self.print_page()
                self.erase_label_column(self.nr_of_labels + 2)
            self.xlSheet.Cells(label_sub_count + 2, 1).Value = self.label_nrs[label_count]

            label_sub_count += 1
            label_count += 1
        self.print_page()

if __name__ == "__main__":
    main_file = "C:\\Users\\ht-afgr7\\Desktop\\PriceTag-master\\PriceTag-master\\test1.xlsm"
    label_file = "C:\\Users\\ht-afgr7\\Desktop\\PriceTag-master\\PriceTag-master\\vorunr.txt"
    label_type = "A6L"

    la = LabelApp(main_file, label_file, label_type)
    la.is_fake_print = True
    la.start_working()
