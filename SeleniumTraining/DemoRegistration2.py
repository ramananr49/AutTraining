from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client")
driver.maximize_window()

register_here_link = driver.find_element(By.LINK_TEXT, "Register here")
try:
    register_here_link.click()
except Exception:
    driver.execute_script("arguments[0].click();", register_here_link)

assert driver.current_url == "https://rahulshettyacademy.com/client/auth/register"
assert driver.find_element(By.CSS_SELECTOR, "h1[class='login-title']").text == "Register"

driver.find_element(By.CSS_SELECTOR, '[id="firstName"]').send_keys("test0204")
driver.find_element(By.CSS_SELECTOR, '[id="lastName"]').send_keys("user0204")
driver.find_element(By.CSS_SELECTOR, '[id="userEmail"]').send_keys("testuser0204@gmail.com")
driver.find_element(By.CSS_SELECTOR, '[id="userMobile"]').send_keys(8144551058)
occupation_dropdown = Select(driver.find_element(By.CSS_SELECTOR, 'select[formcontrolname="occupation"]'))
occupation_dropdown.select_by_index(3)
print(occupation_dropdown.first_selected_option.text)
assert occupation_dropdown.first_selected_option.text == "Engineer"

occupation_dropdown.select_by_value('1: Doctor')
print(occupation_dropdown.first_selected_option.text)
assert occupation_dropdown.first_selected_option.text == "Doctor"

occupation_dropdown.select_by_visible_text("Scientist")
print(occupation_dropdown.first_selected_option.text)
assert occupation_dropdown.first_selected_option.text == "Scientist"

all_options = occupation_dropdown.options
for option in all_options:
    print(option.text)