# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#

import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element(By.ID, 'input_value')
x = x_element.text
y = calc(x)

field = browser.find_element(By.ID, 'answer')
field.send_keys(calc(x))

checkbox = browser.find_element(By.ID, 'robotCheckbox')
checkbox.click()

radio = browser.find_element(By.ID, 'robotsRule')
radio.click()

button = browser.find_element(By.TAG_NAME, 'button')
button.click()

time.sleep(10)

browser.quit()