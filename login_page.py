# здесь описываете методы, которые можно использовать на странице логина

from pages.base_page import BasePage
from utils.locators import *
from pages.base_page import BasePage
from utils.locators import *

class LoginPage(BasePage):
    def __init__(self, driver):
        self.locator = LoginPageLocators
        super().__init__(driver)