# здесь описываете методы, которые можно использовать на странице корзины


from selenium import webdriver
import unittest
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.keys import Keys
import config
import locators



class CartPage(BasePage):
    def __init__(self, driver):
        self.locator = CartPageLocators
        super().__init__(driver)