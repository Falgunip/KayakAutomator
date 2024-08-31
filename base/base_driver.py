from selenium.webdriver.support.wait import WebDriverWait

class BaseDriver:
    def __init__(self, driver,wait_time=10):
        self.driver = driver
        self.wait = WebDriverWait(driver,wait_time)