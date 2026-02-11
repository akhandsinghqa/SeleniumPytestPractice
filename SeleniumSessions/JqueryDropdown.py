import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")

try:
    def select_dropdown_values(options_list, values):
        # for "all" scenario
        if "all" in values:
            for option in options_list:
                option.click()
            return

        # for multiple selection scenario
        count = 0
        total = len(values)
        for options in options_list:
            source_value = options.text.strip()
            print("Checked the : ", source_value)
            if source_value in values:
                # print("Checked the : ", source_value)
                options.click()
                count += 1
                if count == total:
                    break


    multi_one_ele = driver.find_element(By.CSS_SELECTOR, "#justAnInputBox + button")
    multi_one_ele.click()
    list_multi_one_ele = driver.find_elements(By.XPATH,
                                              ".//input[@id='justAnInputBox']/../following-sibling::div/ul//span[@data-id]")
    first_choice = ["choice 1", "choice 2 1"]
    select_dropdown_values(list_multi_one_ele, first_choice)

    time.sleep(2)
    multi_two_ele = driver.find_element(By.CSS_SELECTOR, "#justAnInputBox1 + button")
    multi_two_ele.click()
    list_multi_two_ele = driver.find_elements(By.XPATH,
                                              ".//input[@id='justAnInputBox1']/../following-sibling::div/ul//span[@data-id]")
    second_choice = ["all"]
    select_dropdown_values(list_multi_two_ele, second_choice)

    time.sleep(2)
    multi_three_ele = driver.find_element(By.CSS_SELECTOR, "#justAnotherInputBox + button")
    multi_three_ele.click()
    list_multi_three_ele = driver.find_elements(By.XPATH,
                                                ".//input[@id='justAnotherInputBox']/../following-sibling::div/ul//span[@data-id]")
    third_choice = ["choice 1"]
    select_dropdown_values(list_multi_three_ele, third_choice)

finally:
    time.sleep(5)
    driver.quit()
