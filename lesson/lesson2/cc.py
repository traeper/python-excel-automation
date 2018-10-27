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

access_url = "https://quasar.aka.amazon.com/query"
path_prefix = "c:/Python"
dir_prefix = "C:\\Python"
sql_file = "Quasar_appointments.sql"
csv_path = "C:\\Users\\ijiyoun\\Documents\\Query"
csv_file = "ALL_OPS_Document_InboundSchedule_LawData_18W40.csv"
download_file_prefix = "part-"
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

# Remove old csv file
for file in glob.glob(csv_path + "\\" + csv_file):
    os.remove(file)
    print(datetime.now().strftime('%Y/%m/%d %H:%M:%S') + " : Deleted : " + file)

# Access the URL by Chrome
driver = webdriver.Chrome(path_prefix + "/chromedriver.exe", chrome_options=chromeOptions)
driver.get(access_url)
print(datetime.now().strftime(
    '%Y/%m/%d %H:%M:%S') + " : Chrome Opened - URL: " + access_url + ", Download Folder = " + csv_path)

time.sleep(wait_after_reload)

# For test
# download_btn = driver.find_elements_by_class_name("btn")
# download_btn[4].click()

sql = driver.find_element_by_id("fileElem")
sql.send_keys(dir_prefix + "\\" + sql_file)
print(datetime.now().strftime('%Y/%m/%d %H:%M:%S') + " : SQL File = " + dir_prefix + "\\" + sql_file)

time.sleep(wait_after_action)

out_format = driver.find_element_by_xpath("//input[@value='CSV']")
out_format.click()
print(datetime.now().strftime('%Y/%m/%d %H:%M:%S') + " : Chosen CSV")

time.sleep(wait_after_action)

sql_submit = driver.find_element_by_id("submit")
sql_submit.click()
print(datetime.now().strftime('%Y/%m/%d %H:%M:%S') + " : Query Submitted")

print(datetime.now().strftime('%Y/%m/%d %H:%M:%S') + " : Waiting for the Job Gets Done")
for i in range(int(timeout / wait_while_loop)):
    time.sleep(wait_after_reload)
    driver.refresh()
    time.sleep(wait_while_loop - wait_after_reload)

    download_btn = driver.find_elements_by_class_name("btn")
    print(datetime.now().strftime('%Y/%m/%d %H:%M:%S') + " : Clicked Download")

    try:
        download_btn[4].click()

    except WebDriverException:
        print(datetime.now().strftime('%Y/%m/%d %H:%M:%S') + " : Download Button is not clickable")
        continue
    else:
        break

print(datetime.now().strftime('%Y/%m/%d %H:%M:%S') + " : CSV File Downloaded")

time.sleep(wait_after_reload)

# Rename csv file
for file in glob.glob(csv_path + "\\" + download_file_prefix + "*.csv"):
    os.rename(file, csv_path + "\\" + csv_file)
    print(datetime.now().strftime(
        '%Y/%m/%d %H:%M:%S') + " : Renamed the CSV File from" + file + " to " + csv_path + "\\" + csv_file)

time.sleep(wait_after_action)

driver.close()

print(datetime.now().strftime('%Y/%m/%d %H:%M:%S') + " : Chrome Closed")
print(datetime.now().strftime('%Y/%m/%d %H:%M:%S') + " : Batch Completed")