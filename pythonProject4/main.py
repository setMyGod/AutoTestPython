import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/find_link_text"
browser = webdriver.Chrome()
browser.get(link)
somelink = browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
somelink.click()

firstname = browser.find_element(By.NAME, 'first_name')
firstname.send_keys("Ivan")
lastname = browser.find_element(By.NAME, 'last_name')
lastname.send_keys("Hrytsyna")
city = browser.find_element(By.CLASS_NAME, 'city')
city.send_keys("Sumy")
country = browser.find_element(By.ID, 'country')
country.send_keys("Ukraine")
button = browser.find_element(By.CSS_SELECTOR, "button")
button.click()
time.sleep(30)
browser.quit()
