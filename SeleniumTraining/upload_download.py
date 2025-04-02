import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/upload-download-test/index.html")
driver.find_element(By.ID, "downloadButton").click()
filepath = "C:\\Users\\KT678DL\\Downloads\\download.xlsx"
time.sleep(8)
driver.find_element(By.XPATH, "//input[@type='file']").send_keys(filepath)
locator = (By.XPATH, '//div[@role="alert"]/div[2]')
wait = WebDriverWait(driver, 5)
wait.until(expected_conditions.visibility_of_element_located(locator))
print(driver.find_element(*locator).text)

