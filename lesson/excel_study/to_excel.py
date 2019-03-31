import datetime
import xlrd
from dateutil import parser


def find_date_in_path(path:str, target_datetime_str:str):
    wb = xlrd.open_workbook(path)
    sheet = wb.sheet_by_index(0)

    for row_num in range(sheet.nrows):
        # check this cell is date cell.
        if sheet.cell_type(row_num, 0) == xlrd.XL_CELL_DATE:
            cell_value = sheet.cell_value(row_num, 0)
            dt_tuple = xlrd.xldate_as_tuple(cell_value, wb.datemode)

            # Create datetime object from this tuple of cell.
            found_datetime = datetime.datetime(
                dt_tuple[0], dt_tuple[1], dt_tuple[2],
                dt_tuple[3], dt_tuple[4], dt_tuple[5]
            )

            target_datetime = parser.parse(target_datetime_str)

            if found_datetime == target_datetime:
                return row_num
    return None


find_result = find_date_in_path('xlsx/samsung-payment.xlsx', '2017-01-10')

if find_result is not None:
    print(find_result)

