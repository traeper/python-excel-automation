#
# Example) merge one sheet
#
import openpyxl as op

path1 = 'a.xlsx'

wb = op.load_workbook(filename=path1)
ws = wb.worksheets[0]

ws['B2'].value = 'SAMSUNG'


wb.save(path1)
