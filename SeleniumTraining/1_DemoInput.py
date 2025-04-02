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
driver.find_element(By.CSS_SELECTOR, 'a[href="/edit"]').click()
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "h1[class*='title']")))
title_txt = driver.find_element(By.CSS_SELECTOR, "h1[class*='title']").text
print(title_txt)
assert title_txt == "Input"
assert driver.current_url == "https://letcode.in/edit"
assert "edit" in driver.current_url

"""
Actual Task 
"""
driver.find_element(By.CSS_SELECTOR, '#fullName').send_keys("Ramanan Ramasamy")
driver.find_element(By.CSS_SELECTOR, '#join').send_keys(" Person", Keys.TAB)
act_Value = driver.find_element(By.CSS_SELECTOR, '#getMe').get_attribute("value")
assert act_Value == "ortonikc"
driver.find_element(By.CSS_SELECTOR, "#clearMe").clear()
edit_field_disabled = driver.find_element(By.CSS_SELECTOR, '#noEdit')
driver.execute_script("arguments[0].scrollIntoView(true);", edit_field_disabled)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "#noEdit")))
is_field_enable = edit_field_disabled.is_enabled()
print(is_field_enable)
assert not is_field_enable
text_read_only = driver.find_element(By.CSS_SELECTOR, '#dontwrite')
driver.execute_script("arguments[0].scrollIntoView(true);", text_read_only)
is_read_only = text_read_only.get_dom_attribute("readonly")
print(is_read_only)
assert is_read_only == "true"