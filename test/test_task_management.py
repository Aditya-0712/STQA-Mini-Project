from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service('/usr/local/bin/chromedriver')
driver = webdriver.Chrome(service=service)

def test_create_task():
    driver.get("http://localhost:3000") 

    title_field = driver.find_element(By.NAME, "title")
    description_field = driver.find_element(By.NAME, "description")

    title_field.send_keys("Test Task")
    description_field.send_keys("This is a task created by Selenium script.")
    submit_button = driver.find_element(By.ID, "add-task")
    submit_button.click()

    time.sleep(2)

test_create_task()

driver.quit()