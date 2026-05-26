import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from utilities.ReadProperties import ReadConfig


@pytest.fixture() 
def setup():

    browser = ReadConfig.getBrowser()

    if browser == "chrome":

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )

    elif browser == "headless":

        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )

    else:

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )

    driver.maximize_window()

    yield driver

    driver.quit()
