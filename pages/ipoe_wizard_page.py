# -*- coding: utf-8 -*-
from .base_page import BasePage
from .locators import WizardPageLocators

class IPOEWizardPage(BasePage):
    def should_choose_ipoe_connection_type(self):
        self.is_element_present_click(*WizardPageLocators.SELECT_IPOE_TYPE)
