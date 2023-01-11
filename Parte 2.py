# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 11:58:41 2023

@author: Santiago Tovar Perilla
"""

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

# login

options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
driver = webdriver.Firefox(
    executable_path=r'C:\WebDrivers\geckodriver.exe', options=options)


driver.get("https://dineshvelhal.github.io/testautomation-playground/advanced.html")

#lines = driver.find_element_by_class_name('star_rating')
lines = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((
    By.XPATH, "//*[@class='star_rating']"))).text


print(lines)
txt_rating_input = driver.find_elements("xpath", "//*[@id='txt_rating']")[0]
txt_rating_input.send_keys(lines)

check_rating_button = driver.find_element("xpath", "//*[@id='check_rating']")
check_rating_button.click()
