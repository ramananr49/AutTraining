from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element(By.NAME, "name").send_keys("Ramanan")
driver.find_element(By.NAME, "email").send_keys("demo@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("hello@123")
driver.find_element(By.CSS_SELECTOR, "[type='checkbox']").click()
driver.find_element(By.XPATH, '//input[@value="Submit"]').click()
message = driver.find_element(By.XPATH, '//div[contains(@class, "alert-success")]').text
assert "Success!" in message
driver.find_element(By.XPATH, '(//input[@type="text"])[3]').clear()
driver.get_screenshot_as_png()