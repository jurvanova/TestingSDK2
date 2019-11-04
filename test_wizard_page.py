#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .pages.base_page import BasePage
from .pages.wizard_page import WizardPage
from .pages.ipoe_wizard_page import IPOEWizardPage
import pytest
import time

LINK = 'http://192.168.0.1/'

@pytest.mark.wizard_test
class TestWizard():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = WizardPage(browser, LINK)
        page.open()
        time.sleep(3)
        
    @pytest.mark.ipoe      
    def test_wizard_first(self, browser):
        page = WizardPage(browser, browser.current_url)
        page.should_see_first_message()
        time.sleep(2)
        page.should_be_russian_language()
        page.should_press_next_button()
        page.should_choose_mode_standalone()
        page.should_press_next_button_1()
        page = IPOEWizardPage(browser, browser.current_url)
        page.should_choose_ipoe_connection_type()
        
