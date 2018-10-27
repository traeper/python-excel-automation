#
# Example) generate xlsx from csv with compatibility
#

from util import excel_util

# absolute path
dir_path = '/Users/jaymac/PycharmProjects/excel_automation/lesson/lesson2/csv'

# relative path
# dir_path = 'csv'

excel_util.generate_xlsx_from_csv(dir_path)

