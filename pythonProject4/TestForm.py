import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()
browser.get(link)
input1 = browser.find_element(By.CSS_SELECTOR, 'body > div > form > div.first_block > div.form-group.first_class > input')
input1.send_keys('Ivan')

input2 = browser.find_element(By.CSS_SELECTOR, 'body > div > form > div.first_block > div.form-group.second_class > input')
input2.send_keys('Sokolov')

input3 = browser.find_element(By.CSS_SELECTOR, 'body > div > form > div.first_block > div.form-group.third_class > input')
input3.send_keys('gis20072017@gmail.com')

time.sleep(5)

button = browser.find_element(By.CSS_SELECTOR, 'button')
button.click()
time.sleep(5)

welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
welcome_text = welcome_text_elt.text

assert "Congratulations! You have successfully registered!" == welcome_text
time.sleep(10)
browser.quit()

