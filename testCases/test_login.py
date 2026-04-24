from pageObjects.LoginPage import LoginPage
from utilities.readConfig import ReadConfig

def test_login(setup):
 lp = LoginPage(setup)
 lp.setUsername(ReadConfig.getUsername())
 lp.setPassword(ReadConfig.getPassword())
 lp.clickLogin()

assert "dashboard" in setup.current_url
