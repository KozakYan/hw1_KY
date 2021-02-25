
from selenium import webdriver
import unittest
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.keys import Keys
import config
import locators


path = (config.path['path'])





class BaseTestCase(unittest.TestCase): # базовые кейсы для всех тестов

    def setUp(self):
        self.driver = webdriver.Chrome(path)
        self.driver.get(config.links['login_link'])
        self.driver.set_window_size(1920, 1080)
        time.sleep(1)

    def sing_in(self):
        button_sing_in = driver.find_element_by_xpath(locators.Sing_in_objects['button_sing_in'])
        button_sing_in.click()
        time.sleep(1)
        input_for_email = driver.find_element_by_xpath(locators.Sing_in_objects['input_for_email'])
        input_for_email.send_keys(config.authorization_data['email'])
        input_for_password = driver.find_element_by_xpath(locators.Sing_in_objects['input_for_password'])
        input_for_password.send_keys(config.authorization_data['password'])
        button_submit_for_sing_in = driver.find_element_by_xpath(locators.Sing_in_objects['button_submit_for_sing_in'])
        button_submit_for_sing_in.click()
        time.sleep(1)
        button_sing_in = driver.find_element_by_xpath(locators.Sing_in_objects['button_sing_in'])
        button_sing_in.click()
        time.sleep(2)
        LK_title = driver.find_element_by_xpath(locators.LK_objects['LK_title'])
        LK_title.is_displayed()

    def log_out(self):
        self.driver.get(config.links['lk_link'])
        button_logout = driver.find_element_by_xpath(locators.LK_objects['button_logout'])
        button_logout.click()
        button_sing_in.click()
        input_for_email.is_displayed()

    def add_product_to_cart(self):
        self.driver.get(config.links['catalog_link'])
        button_ad_dto_cart = driver.find_element_by_xpath(locators.Catalog['button_ad_dto_cart'])
        button_ad_dto_cart.click()
        basket_button = driver.find_element_by_xpath(locators.Basket['basket_button'])
        basket_button.click()

    def delete_product(self):
        button_delete_product = driver.find_element_by_xpath(locators.Basket['button_delete_product'])
        button_delete_product.click()

    def check_the_item_in_the_cart(self):
        block_product = driver.find_element_by_xpath(locators.Basket['block_cost'])
        block_product.is_displayed()

















    def tearDown(self):
        self.driver.quit()






if __name__ == '__main__':
    unittest.main()










