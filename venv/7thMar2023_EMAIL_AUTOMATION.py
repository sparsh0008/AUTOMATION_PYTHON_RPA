# import openpyxl module
import openpyxl

# Give the location of the file
path = "Bonus Calculation Sheet  Sample Dataset.xlsx"


wb_obj = openpyxl.load_workbook(path)

sheet_obj = wb_obj.active
m_row = sheet_obj.max_row
m_col = sheet_obj.max_column

for i in range(2, m_row + 1):
    for j in range(1, m_col+1):
        cell_obj = sheet_obj.cell(row=i, column=j)
    #     print(cell_obj.value, end=" ")
    # print("\n", end="")

for i in range(2, m_row+1):
    cell_obj = sheet_obj.cell(row=i, column=m_col)
    print(cell_obj, end="\n")
