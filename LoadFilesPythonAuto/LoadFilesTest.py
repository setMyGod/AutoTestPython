from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/file_input.html')

name = browser.find_element(By.NAME, 'firstname').send_keys('Ivan')
lastName = browser.find_element(By.NAME, 'lastname').send_keys('Hrytsyna')
email = browser.find_element(By.NAME, 'email').send_keys('gis20072017@gmail.com')

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'about.txt')
elements = browser.find_element(By.ID, 'file')
elements.send_keys(file_path)
browser.find_element(By.XPATH, '/html/body/div/form/button').click()
