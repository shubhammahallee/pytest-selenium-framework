import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://demoqa.llq.vn/radio-button")

wait = WebDriverWait(driver,10)

wait.until(EC.element_to_be_clickable((By.ID,"radio2"))).click()
time.sleep(1)

wait.until(EC.element_to_be_clickable((By.ID,"radio1"))).click()
time.sleep(1)








driver.get("https://demoqa.llq.vn/checkbox")

wait.until(EC.element_to_be_clickable((By.XPATH,"//label[@class='hierarchy-root-label']"))).click()
time.sleep(1)


driver.get("https://demoqa.llq.vn/buttons")
wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@id='doubleClickBtn']"))).click()
time.sleep(1)

wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@id='KOpYw']"))).click()
time.sleep(1)

wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@id='rightClickBtn']"))).click()
time.sleep(1)






driver.get("https://demoqa.llq.vn/upload-download")

wait.until(EC.element_to_be_clickable((By.XPATH,"//a[@id='downloadButton']"))).click()
time.sleep(1)

driver.find_element(By.XPATH, "//input[@id='uploadFile']").send_keys(r"C:\Users\Shubham\Desktop\PARA_BANK\Screenshots\login_success.png")
time.sleep(5)

driver.get("https://demoqa.llq.vn/dynamic-properties")
wait.until(EC.element_to_be_clickable((By.ID,"enableAfter"))).click()
time.sleep(6)

wait.until(EC.element_to_be_clickable((By.ID,"colorChange"))).click()
time.sleep(1)

wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='visibleAfter']"))).click()
time.sleep(6)



driver.quit()

