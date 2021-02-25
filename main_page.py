# здесь описываете методы, которые можно использовать на главной

from pages.base_page import BasePage
from utils.locators import *
from pages.base_page import BasePage
from utils.locators import *

class MainPage(BasePage):
    def __init__(self, driver):
        self.locator = MainPageLocators
        super().__init__(driver)

    def check_mainpage_loaded(self):
        return True if self.find_element(*self.locator.LOGO) else False


