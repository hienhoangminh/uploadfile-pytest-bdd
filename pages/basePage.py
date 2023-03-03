from selenium.webdriver.support.ui import WebDriverWait

class BasePage():
    def __init__(self, browser):
        self._browser = browser
        self._wait = WebDriverWait(self._browser, 30)
        
    def __isAt__(self):
        pass