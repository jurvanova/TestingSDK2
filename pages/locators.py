from selenium.webdriver.common.by import By

class BasePageLocators():
    pass

class WizardPageLocators():
    FIRST_PAGE_MESSAGE = (By.CSS_SELECTOR, '.caption')
    FIRST_PAGE_BUTTON = (By.CSS_SELECTOR, '[ng-click="customNextStep()"]')
    LANGUAGE_MESSAGE = (By.CSS_SELECTOR, '.geo-caption.noselect.ng-binding')
    BUTTON_NEXT_YES = (By.CSS_SELECTOR, '[ng-click="yes()"]')
    BUTTON_NEXT = (By.CSS_SELECTOR, '[ng-click="customNext()"]')
    SELECT_STANDALONE = (By.CSS_SELECTOR, '[value="standalone"]')
    BUTTON_NEXT_1 = (By.CSS_SELECTOR, '.next.ng-binding')
    SELECT_IPOE_TYPE = (By.CSS_SELECTOR, '[value="0"]')
    
    
