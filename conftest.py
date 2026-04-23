improt pytest
from selenium import webdriver
from utilities.properties import readconfig

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
    driver = webdriver.Chrome(options=options)
  else:
        driver. webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

  
    
