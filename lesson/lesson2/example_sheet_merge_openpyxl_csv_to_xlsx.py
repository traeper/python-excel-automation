#
# Example) merge one sheet
#

from util import excel_util, filename_util

# absolute path
dir_path = '/Users/jaymac/PycharmProjects/excel_automation/lesson/lesson2/csv'

# 1. generate_xlsx_from_csv
excel_util.generate_xlsx_from_csv(dir_path)

# 2. find all xlsx files
found_paths = filename_util.find_files_by_extension(dir_path, 'xlsx')

# 3. merge all xlsx files
excel_util.generate_merged_xlsx_file(found_paths, dir_path + '/all_merged.xlsx')

# 4. check the merged..
