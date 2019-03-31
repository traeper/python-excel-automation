import datetime
import xlrd
from dateutil import parser


def search_row_of_date_in_excel(path: str, target_datetime_str: str):
    wb = xlrd.open_workbook(path)
    sheet = wb.sheet_by_index(0)

    for index in range(sheet.nrows):
        # check this cell is date cell.
        # start (0,0) not (1,1)
        if sheet.cell_type(index, 0) == xlrd.XL_CELL_DATE:
            cell_value = sheet.cell_value(index, 0)
            datetime_tuple = xlrd.xldate_as_tuple(cell_value, wb.datemode)

            # date vs datetime
            # date : 2019-01-01, datetime : 2019-01-01 10:00:00

            # Create datetime object from this tuple of cell.
            found_datetime = datetime.datetime(
                datetime_tuple[0], datetime_tuple[1], datetime_tuple[2],
                datetime_tuple[3], datetime_tuple[4], datetime_tuple[5]
            )

            # parse date string like '2018-09-11' and extract datetime
            target_datetime = parser.parse(target_datetime_str)

            if found_datetime == target_datetime:
                row_num = index + 1
                return row_num
    return None


found_row = search_row_of_date_in_excel('xlsx/samsung-payment.xlsx', '2017-02-25')

if found_row is not None:
    print(found_row)
