import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

wait= WebDriverWait(driver,10)

driver.get("https://demoqa.llq.vn/login")

wait.until(EC.visibility_of_element_located((By.ID,"userName"))).send_keys("sumon")
wait.until(EC.visibility_of_element_located((By.ID,"password"))).send_keys("remo")
wait.until(EC.element_to_be_clickable((By.ID,"login"))).click()

driver.save_screenshot(r"C:\Users\Shubham\Desktop\PARA_BANK\Screenshots\login_success.png")
time.sleep(3)

wait.until(EC.element_to_be_clickable((By.ID,"newUser"))).click()
wait.until(EC.element_to_be_clickable((By.ID,"gotologin"))).click()
wait.until(EC.element_to_be_clickable((By.ID,"newUser"))).click()
time.sleep(3)


wait.until(EC.visibility_of_element_located((By.ID,"email"))).send_keys("sumon")
wait.until(EC.visibility_of_element_located((By.ID,"userName"))).send_keys("sumon")
wait.until(EC.visibility_of_element_located((By.ID,"password"))).send_keys("remo")
wait.until(EC.element_to_be_clickable((By.ID,"register"))).click()
driver.save_screenshot(r"C:\Users\Shubham\Desktop\PARA_BANK\Screenshots\register_success.png")
time.sleep(3)



driver.get("https://demoqa.llq.vn/books")

wait.until(EC.element_to_be_clickable((By.ID,"login"))).click()

wait.until(EC.visibility_of_element_located((By.ID,"userName"))).send_keys("sumon")
wait.until(EC.visibility_of_element_located((By.ID,"password"))).send_keys("remo")
wait.until(EC.element_to_be_clickable((By.ID,"login"))).click()


driver.quit()


