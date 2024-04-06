from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.psegameshop.com/my-account/")
driver.maximize_window()
username = driver.find_element(By.ID, "username")
username.clear()
username.send_keys("")
password = driver.find_element(By.ID, "password")
password.clear()
password.send_keys("")
login = driver.find_element(By.NAME, "login")
login.click()

driver.close()


