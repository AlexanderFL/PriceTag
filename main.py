# Works with python version 3.6.4

import win32com.client as win32
from time import sleep

main_file = "C:\\Users\\ht-afgr7\\Desktop\\PriceTag-master\\PriceTag-master\\test1.xlsm"
label_file = "vorunr.txt"
label_type = "Verdmidar"


def reset_label_column(sheet, stop=14):
    for x in range(2, stop):
        sheet.Cells(x, 1).Value = None


label_number = 0


def get_label_number():
    if label_type is "VerdmidarLitlir":
        return 12
    elif label_type is "Verdmidar":
        return 12
    elif label_type is "A7":
        return 8
    elif label_type is "A6":
        return 4
    elif label_type is "A6L":
        return 2
    elif label_type is "A6B":
        return 4
    elif label_type is "A5":
        return 2


label_number = get_label_number()

# Opening excel and setting the active worksheet
excel = win32.gencache.EnsureDispatch('Excel.Application')
excel.Interactive = True
excel.Visible = True
excel.DisplayAlerts = True

xlBook = excel.Workbooks.Open(main_file)
xlSheet = xlBook.Worksheets('Front')

# Open label file
codes = []
with open(label_file) as f:
    codes = f.read().splitlines()

# Placing all of the labels and printing
label_type = 12
label_count = 0
label_sub_count = 0
while label_count != len(codes):
    if label_sub_count % label_number == 0 and label_count is not 0:
        label_sub_count = 0
        xlSheet = xlBook.Worksheets(label_type)
        # xlSheet.PrintOut(Copies=1, Collate=True)
        sleep(1)
        xlSheet = xlBook.Worksheets('Front')
        reset_label_column(xlSheet, label_number+2)
    xlSheet.Cells(label_sub_count+2,1).Value = codes[label_count]

    label_sub_count += 1
    label_count += 1
xlSheet = xlBook.Worksheets(label_type)
# xlSheet.PrintOut(Copies=1, Collate=True)
xlSheet = xlBook.Worksheets('Front')

# xlBook.Application.Run('test1.xlsm!RefreshQuery')
xlBook.Close(True)
excel.Quit()
