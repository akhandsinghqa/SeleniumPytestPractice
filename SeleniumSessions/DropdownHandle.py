import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.orangehrm.com/en/30-day-free-trial")

try:
    def select_dropdown(element):
        return Select(element)


    def select_value(element, value):
        return select_dropdown(element).select_by_value(value)


    # select_value(driver.find_element(By.ID,"Form_getForm_Country"),"India")
    dropdown_ele = driver.find_element(By.ID, "Form_getForm_Country")
    country_dropdown = select_dropdown(dropdown_ele)
    country_options = country_dropdown.options
    print(len(country_options))
    # country_dropdown.select_by_visible_text("India")
    for option in country_options:
        country = option.text
        # print(country,sep="/t")
        if "India" in country:
            print("Found : ", country)
            # country_dropdown.select_by_visible_text("India")
            # country_dropdown.select_by_value("India")
            # country_dropdown.select_by_index(43)
            print(country_dropdown.is_multiple)
            break


    def custom_select(options_list, value):
        print(len(options_list))
        for ele in options_list:
            if ele.text == value:
                ele.click()
                break


    list_ele = driver.find_elements(By.CSS_SELECTOR, "#Form_getForm_Country option")
    custom_select(list_ele, "India")

finally:
    time.sleep(5)
    driver.quit()
