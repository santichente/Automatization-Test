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

driver.get("https://dineshvelhal.github.io/testautomation-playground/login.html")
username_input = driver.find_elements("xpath", "//*[@id='user']")[0]
username_input.send_keys("admin")

password_input = driver.find_elements("xpath", "//*[@id='password']")[0]
password_input.send_keys("admin")

login_button = driver.find_element("xpath", "//*[@id='login']")
login_button.click()

# seleccion 1
rad_small = driver.find_element("xpath", "//*[@id='rad_small']")
rad_small.click()

select_flavor = Select(WebDriverWait(driver, 20).until(EC.element_to_be_clickable((
    By.XPATH, "//*[@id='select_flavor']"))))
select_flavor.select_by_value('Supreme')

rad_barbeque = driver.find_element("xpath", "//*[@id='rad_barbeque']")
rad_barbeque.click()

tomoto = driver.find_element("xpath", "//*[@id='tomoto']")
tomoto.click()

quantity = driver.find_elements("xpath", "//*[@id='quantity']")[0]
quantity.send_keys("2")

submit_button = driver.find_element("xpath", "//*[@id='submit_button']")
submit_button.click()

time.sleep(7)
# seleccion 2


rad_medium = driver.find_element("xpath", "//*[@id='rad_medium']")
rad_medium.click()

select_flavor.select_by_value('Pepperoni')

rad_barbeque.click()

green_olive = driver.find_element("xpath", "//*[@id='green_olive']")
green_olive.click()

onions = driver.find_element("xpath", "//*[@id='onions']")
onions.click()

quantity.send_keys((Keys.CONTROL + 'a', Keys.BACKSPACE))
quantity.send_keys("-21")

submit_button = driver.find_element("xpath", "//*[@id='submit_button']")
submit_button.click()
