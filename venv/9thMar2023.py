# Import Modules
from openpyxl import Workbook

# Active Workbook
wb = Workbook()
sheet = wb.active

# Data Tuple
data = (
    # max_col-3, max_col-2, max_col-1,max_col
    ("Name", "CA1", "CA2", "CA3"),
    ("RAHUL", 20, 30, 21),
    ("VIKAS", 12, 23, 29),
    ("RAHUL", 20, 30, 28),
    ("VIKAS", 12, 23, 27),
    ("RAHUL", 20, 30, 22),
    ("VIKAS", 12, 23, 20)
)

# For Loop To Append the Data
for row in data:
    sheet.append(row)

# Max Rows and Max Column
max_row = sheet.max_row
max_col = sheet.max_column

# Total Keyword
cell = sheet.cell(row=max_row + 1, column=max_col - 3)
cell.value = "TOTAL"
cf = cell.font
cf = cell.font.copy(bold=True)

# Total For CA1
cell = sheet.cell(row=max_row + 1, column=max_col - 2)
cell.value = "=SUM(B2:B7)"
cf = cell.font
cell.font = cf.copy(bold=True)

# Total For CA2
cell = sheet.cell(row=max_row + 1, column=max_col - 1)
cell.value = "=SUM(C2:C7)"
cf = cell.font
cell.font = cf.copy(bold=True)

# Total For CA3
cell = sheet.cell(row=max_row + 1, column=max_col)
cell.value = "=SUM(D2:D7)"
cf = cell.font
cell.font = cf.copy(bold=True)

# To Save the Workbook as Student.xlsx
wb.save("Student.xlsx")
