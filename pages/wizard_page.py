# -*- coding: utf-8 -*-
from .base_page import BasePage
from .locators import WizardPageLocators


class WizardPage(BasePage):
    def should_see_first_message(self):
        assert self.is_element_present(*WizardPageLocators.FIRST_PAGE_MESSAGE), 'Page not opened!'
        self.is_element_present_click(*WizardPageLocators.FIRST_PAGE_BUTTON)
        
    def should_be_russian_language(self):
        assert self.browser.find_element(*WizardPageLocators.LANGUAGE_MESSAGE).text == 'Возможно, ваш язык Русский?', 'Language is incorrect'
        self.is_element_present_click(*WizardPageLocators.BUTTON_NEXT_YES)        
        
    def should_press_next_button(self):
        self.is_element_present_click(*WizardPageLocators.BUTTON_NEXT)
        
    def should_choose_mode_standalone(self):
        self.is_element_present_click(*WizardPageLocators.SELECT_STANDALONE)
        
    def should_press_next_button_1(self):
        self.is_element_present_click(*WizardPageLocators.BUTTON_NEXT_1)
    
