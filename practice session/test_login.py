
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://practicetestautomation.com/practice-test-login/")

wait = WebDriverWait(driver,10)

driver.find_element(By.ID,"username").send_keys("student")
driver.find_element(By.ID,"password").send_keys("Password123")

time.sleep(2)  

wait.until(EC.element_to_be_clickable((By.ID, "submit"))).click()

driver.save_screenshot(r"C:\Users\Shubham\Desktop\PARA_BANK\Screenshots\login_success.png")

driver.maximize_window()

assert "logged-in-successfully" in driver.current_url



driver.quit()
