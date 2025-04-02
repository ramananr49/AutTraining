import time
from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client")
driver.maximize_window()
print(driver.title)
expectedLandingURL = "https://rahulshettyacademy.com/client/auth/login"
landingURL = driver.current_url
assert landingURL == expectedLandingURL
Register_Here_Link = driver.find_element(By.LINK_TEXT, "Register here")
try:
    Register_Here_Link.click()
except ElementClickInterceptedException as e:
    driver.execute_script("arguments[0].click();", Register_Here_Link)
time.sleep(2)
registerPageURL = driver.current_url
assert registerPageURL == "https://rahulshettyacademy.com/client/auth/register"

driver.back()
assert expectedLandingURL == driver.current_url
time.sleep(2)

driver.forward()
assert registerPageURL == driver.current_url
time.sleep(2)