#
# search all files by extension.
#
import glob
import os.path

# myPath = ''
# myExt = '*.xlsx'
#
# filename_array = []
# filename_except_extension_array = []
#
# for filename in glob.glob(os.path.join(myPath, myExt)):
#     # full filename
#     filename_array.append(filename)
#
#     # filename except extension
#     filename_except_extension = os.path[os.path.rfind('/') + 1:]
#     filename_except_extension_array.append(filename_except_extension)
#
# print filename_array
# print filename_except_extension_array

#
# today, total url of corp file
#

import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException
from datetime import datetime
import time
import shutil
import glob
import os


def do_core(access_url, corp_name):
    # access_url = "https://unified-portal-fe.corp.amazon.com/#/appointment?searchType=REQUESTED_DELIVERY&searchCategory=date&fc=NRT1&fromDate=1540047600000&toDate=1540306800000"
    path_prefix = "c:/Python"
    dir_prefix = "C:\\Python"
    csv_path = "C:\\Users\\ijiyoun\\Documents\\Query"
    csv_file = corp_name + ".resources"
    download_file_prefix = "appointmentSearch"
    wait_after_action = 3
    wait_after_reload = 15
    wait_while_loop = 60
    timeout = 3600

    # Chrome Configuration
    chromeOptions = webdriver.ChromeOptions()
    # Set Default Download Folder
    prefs = {"download.default_directory": csv_path}
    chromeOptions.add_experimental_option("prefs", prefs)

    print(datetime.now().strftime('%Y/%m/%d %H:%M:%S') + " : Batch Started")

    # Remove old resources file
    for file in glob.glob(csv_path + "\\" + csv_file):
        os.remove(file)
        print(datetime.now().strftime('%Y/%m/%d %H:%M:%S') + " : Deleted : " + file)

        # Access the URL by Chrome
    driver = webdriver.Chrome(path_prefix + "/chromedriver.exe", chrome_options=chromeOptions)
    driver.get(access_url)
    print(datetime.now().strftime(
        '%Y/%m/%d %H:%M:%S') + " : Chrome Opened - URL: " + access_url + ", Download Folder = " + csv_path)

    time.sleep(wait_after_reload)

    excel_submit = driver.find_element_by_xpath(
        '/html/body/up-app/mat-sidenav-container/mat-sidenav-content/div/div[2]/up-appointment/div/up-appointment-result-panel/mat-accordion/mat-expansion-panel/mat-expansion-panel-header/span/mat-panel-title/div/button[2]')
    excel_submit.click()

    print(datetime.now().strftime('%Y/%m/%d %H:%M:%S') + " : CSV File Downloaded")

    time.sleep(wait_after_reload)

    # Rename resources file
    for file in glob.glob(csv_path + "\\" + download_file_prefix + "*.resources"):
        os.rename(file, csv_path + "\\" + csv_file)
        print(datetime.now().strftime(
            '%Y/%m/%d %H:%M:%S') + " : Renamed the CSV File from" + file + " to " + csv_path + "\\" + csv_file)

    time.sleep(wait_after_action)

# declare corp name array
corp_names = ['NRT1', 'FSZ1']

# get start, end timestamp of today
start_str = time.strftime("%m/%d/%Y") + " 00:00:00"
end_str = time.strftime("%m/%d/%Y ") + " 23:59:59"
start_ts = int(time.mktime(time.strptime(start_str, "%m/%d/%Y %H:%M:%S")))
end_ts = int(time.mktime(time.strptime(end_str, "%m/%d/%Y %H:%M:%S")))

print (start_ts)
print (end_ts)

# for iteration loop
for corp_name in corp_names:
    access_url = "https://unified-portal-fe.corp.amazon.com/#/appointment?searchType=REQUESTED_DELIVERY&searchCategory=date&fc={}&fromDate={}&toDate={}" \
        .format(corp_name, str(start_ts) + '000', str(end_ts) + '000')

    print (access_url)
    # then for loop - the core logic
    do_core(access_url, corp_name)


