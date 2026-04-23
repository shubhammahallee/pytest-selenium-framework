improt pytest
from selenium import webdriver
from utilities.properties import readconfig
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def setup():
  browser = readconfig.getBrowser()
  if browser == "Chrome":
    driver = webdriver.Chrome()
  elif browser == "Firefox":
    driver = webdriver.Firefox()  
  elif browser == "headless":
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")  
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=options)
  else:
        driver. webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

  
    
