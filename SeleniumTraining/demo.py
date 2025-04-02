from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# ch_option = Options()
# ch_option.add_argument("--ignore-certificate-errors")
# driver = webdriver.Chrome(options=ch_option)
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client/auth/login")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

# url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
# driver = webdriver.Chrome()
# driver.get(url)
# driver.maximize_window()
# titleTxt = driver.title
# print(titleTxt)
# print(driver.current_url)
# assert url == driver.current_url