import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
PATH = os.path.join(PROJECT_ROOT, "driver/chromedriver")

driver = webdriver.Chrome(PATH)

driver.get('https://aaygupta.com/todo')
todo_input = driver.find_element_by_class_name('todo-input')
todo_input.send_keys('Apple')

# add_button = driver.find_element_by_class_name('todo-button')
# add_button.click()

todo_input.send_keys(Keys.ENTER)