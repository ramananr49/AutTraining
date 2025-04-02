from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://letcode.in/")

wait = WebDriverWait(driver, 4)

driver.find_element(By.XPATH, '//a[@href="/test" and @class="navbar-item"]').click()
driver.find_element(By.CSS_SELECTOR, 'a[href="/button"]').click()
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "h1[class*='title']")))
title_txt = driver.find_element(By.CSS_SELECTOR, "h1[class*='title']").text
print(title_txt)
assert title_txt == "Button"
assert driver.current_url == "https://letcode.in/button"
assert "button" in driver.current_url
"""
Actual Task 
"""
