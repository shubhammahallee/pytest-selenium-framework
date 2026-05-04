import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 10)

"""# ─── Helper: JS click (bypasses overlay/interactability issues) ───────────────
def js_click(element):
    driver.execute_script("arguments[0].click();", element)

# ─── Helper: Scroll into view + JS click ─────────────────────────────────────
def scroll_and_click(element):
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    time.sleep(0.3)
    js_click(element)

# ══════════════════════════════════════════════════════════════════════════════
# PAGE 1 — Text Box
# ══════════════════════════════════════════════════════════════════════════════
driver.get("https://demoqa.llq.vn/text-box")

wait.until(EC.visibility_of_element_located((By.ID, "userName"))).send_keys("VD")
driver.find_element(By.ID, "userEmail").send_keys("vd1980@gmail.com")
driver.find_element(By.ID, "currentAddress").send_keys("kothrud,pune")
driver.find_element(By.XPATH, "//textarea[@id='permanentAddress']").send_keys("kothrud,pune")

# FIX 1: Use JS click on submit — avoids ad banner overlap
submit_btn = driver.find_element(By.ID, "submit")
scroll_and_click(submit_btn)

time.sleep(2)
os.makedirs(r"C:\Users\Shubham\Desktop\PARA_BANK\Screenshots", exist_ok=True)
driver.save_screenshot(r"C:\Users\Shubham\Desktop\PARA_BANK\Screenshots\login_success.png")"""


# ══════════════════════════════════════════════════════════════════════════════
# PAGE 3 — Practice Form
# ══════════════════════════════════════════════════════════════════════════════
driver.get("https://demoqa.llq.vn/browser-windows")











# ══════════════════════════════════════════════════════════════════════════════
# PAGE 2 — Practice Form
# ══════════════════════════════════════════════════════════════════════════════
driver.get("https://demoqa.llq.vn/automation-practice-form")

# ── Name ───────────────────────────────────────────────────────────────────
wait.until(EC.visibility_of_element_located((By.ID, "firstName"))).send_keys("VD")
driver.find_element(By.ID, "lastName").send_keys("VpD")

# ── Email ──────────────────────────────────────────────────────────────────
driver.find_element(By.ID, "userEmail").send_keys("vd1980@gmail.com")

# ── Gender (Male = radio-1, Female = radio-2) ──────────────────────────────
# FIX: your screenshot shows Female is selected — label for='gender-radio-2'
driver.execute_script(
    "arguments[0].click();",
    driver.find_element(By.ID, "gender-radio-2")   # JS click on the input itself
)

# ── Mobile ─────────────────────────────────────────────────────────────────
driver.find_element(By.ID, "userNumber").send_keys("7894561230")

# ── Date of Birth ──────────────────────────────────────────────────────────
dob = wait.until(EC.element_to_be_clickable((By.ID, "dateOfBirthInput")))
dob.click()
time.sleep(0.4)
dob.send_keys(Keys.CONTROL + "a")
dob.send_keys("06 Jan 2000")
dob.send_keys(Keys.TAB)
time.sleep(0.4)

# ── Subjects ───────────────────────────────────────────────────────────────
# FIX: Subjects uses its own input box, NOT select2
subject_input = driver.find_element(By.ID, "subjectsInput")
subject_input.send_keys("Maths")
time.sleep(0.5)
subject_input.send_keys(Keys.ENTER)

# ── Hobbies ────────────────────────────────────────────────────────────────
# FIX: was using 'browser' (undefined) — use 'driver'
driver.execute_script(
    "arguments[0].click();",
    driver.find_element(By.ID, "hobbies-checkbox-1")  # Sports
)
driver.execute_script(
    "arguments[0].click();",
    driver.find_element(By.ID, "hobbies-checkbox-2")  # Reading
)

# ── Upload Picture ─────────────────────────────────────────────────────────
driver.find_element(By.ID, "uploadPicture").send_keys(
    r"C:\Users\Shubham\Desktop\PARA_BANK\Screenshots\login_success.png"
)

# ── Current Address ────────────────────────────────────────────────────────
driver.find_element(By.ID, "currentAddress").send_keys("Kothrud, Pune")

# ── State ──────────────────────────────────────────────────────────────────
# FIX: It's a native <select> tag — use Select(), NOT div click
state_select = wait.until(EC.element_to_be_clickable((By.ID, "state")))
driver.execute_script("arguments[0].scrollIntoView({block:'center'});", state_select)
Select(state_select).select_by_visible_text("NCR")
time.sleep(0.5)  # wait for city to populate

# ── City ───────────────────────────────────────────────────────────────────
city_select = wait.until(EC.element_to_be_clickable((By.ID, "city")))
Select(city_select).select_by_visible_text("Delhi")

# ── Submit ─────────────────────────────────────────────────────────────────
submit_btn = driver.find_element(By.ID, "submit")
driver.execute_script("arguments[0].scrollIntoView({block:'center'});", submit_btn)
time.sleep(0.5)
driver.execute_script("arguments[0].click();", submit_btn)

time.sleep(2)
driver.save_screenshot(r"C:\Users\Shubham\Desktop\PARA_BANK\Screenshots\form_submitted.png")

driver.quit()
