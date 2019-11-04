from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from .locators import BasePageLocators

class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        
    def open(self):
        self.browser.get(self.url)
        self.browser.maximize_window()
        
    def is_element_present(self, how, what):
        try:
            WebDriverWait(self.browser, 3).until(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return False
        return True
        
    def is_disappeared(self, how, what):
        try:
            WebDriverWait(self.browser, 3, 1, TimeoutException).until_not(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return False
        return True
    
    def is_element_present_click(self, how, what):
        try:
            WebDriverWait(self.browser, 3).until(
                EC.presence_of_element_located((how, what))
            ).click()
        except TimeoutException:
            return False
        return True

    
