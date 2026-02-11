import time

import xlrd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def select_dropdown(element):
    return Select(element)


def select_value(element, value):
    return select_dropdown(element).select_by_value(value)


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.orangehrm.com/en/30-day-free-trial")
try:
    username_ele = driver.find_element(By.ID, "Form_getForm_subdomain")
    name_ele = driver.find_element(By.ID, "Form_getForm_Name")
    email_ele = driver.find_element(By.ID, "Form_getForm_Email")
    contact_ele = driver.find_element(By.ID, "Form_getForm_Contact")
    country_ele = driver.find_element(By.ID, "Form_getForm_Country")
    submit_ele = driver.find_element(By.ID, "Form_getForm_action_submitForm")

    workbook = xlrd.open_workbook("RegistrationData.xls")
    sheet = workbook.sheet_by_name("registration")

    # get total number of rows
    row_count = sheet.nrows
    col_count = sheet.ncols
    print("Total Rows : ", row_count)
    print("Total Columns : ", col_count)

    for curr_row in range(1, row_count):
        username = sheet.cell_value(curr_row, 0)
        name = sheet.cell_value(curr_row, 1)
        email = sheet.cell_value(curr_row, 2)
        contact = sheet.cell_value(curr_row, 3)
        country = sheet.cell_value(curr_row, 4)
        username_ele.clear()
        username_ele.send_keys(username)
        name_ele.clear()
        name_ele.send_keys(name)
        email_ele.clear()
        email_ele.send_keys(email)
        contact_ele.clear()
        contact_ele.send_keys(contact)
        # country_ele.clear()
        select_value(country_ele, country)
        # submit_ele.click()
        time.sleep(2)
finally:
    time.sleep(5)
    driver.quit()
