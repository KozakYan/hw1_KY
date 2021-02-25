# здесь находятся тест-кейсы
# один кейс - один def


from selenium import webdriver
import unittest
from base_test_case import *
import time
from selenium.webdriver.common.keys import Keys
import config
import locators
import cart_page

path = (config.path['path'])


class TestSima(BaseTestCase):

    def setUp(self):
        super().setUp()

    def Wrong_and_correct_login(self):
        print("\n" + str(test_cases(1)))
        driver = self.driver
        # логин не правильный
        button_sing_in = driver.find_element_by_xpath(locators.Sing_in_objects['button_sing_in'])
        button_sing_in.click()
        time.sleep(1)
        input_for_email = driver.find_element_by_xpath(locators.Sing_in_objects['input_for_email'])
        input_for_email.send_keys(config.authorization_data['email'])
        input_for_password = driver.find_element_by_xpath(locators.Sing_in_objects['input_for_password'])
        input_for_password.send_keys(config.authorization_data['wrong_password'])
        button_submit_for_sing_in = driver.find_element_by_xpath(locators.Sing_in_objects['button_submit_for_sing_in'])
        button_submit_for_sing_in.click()
        error_login_notification = driver.find_element_by_xpath(locators.Sing_in_objects['error_login_notification'])
        # ОР
        error_login_notification.is_displayed()
        driver.refresh()
        # логин правильный
        super().sing_in()
        # разлогин
        super().log_out()

    def Add_to_cart(self):
        print("\n" + str(test_cases(2)))
        driver = self.driver
        # логин
        super().sing_in()
        # добавление товара в корзину
        super().add_product_to_cart()
        # ОР наличие товара в корзине
        block_product = driver.find_element_by_xpath(locators.Basket['block_cost'])
        block_product.is_displayed()
        # удаление товара из корзины после проверки (постусловие)
        super().delete_product()
        # разлогин
        super().log_out()

    def Add_to_cart_and_check(self):
        print("\n" + str(test_cases(3)))
        driver = self.driver
        # логин
        super().sing_in()
        # добавление товара в корзину
        super().add_product_to_cart()
        # ОР наличие товара в корзине
        super.check_the_item_in_the_cart()
        # Разлогин
        super().log_out()
        # ожидание после разлогина
        time.sleep(60)
        # логин
        super().sing_in()
        #переход к корзине
        basket_button = driver.find_element_by_xpath(locators.Basket['basket_button'])
        basket_button.click()
        # ОР наличие товара в корзине
        super.check_the_item_in_the_cart()
        # удаление товара из корзины после проверки (постусловие)
        super().delete_product()
        # разлгин (постусловие)
        super().log_out()

    def Add_to_cart_check_and_delete(self):
        print("\n" + str(test_cases(4)))
        driver = self.driver
        # логин
        super().sing_in()
        # добавление товара в корзину
        super().add_product_to_cart()
        # ОР наличие товара в корзине
        super.check_the_item_in_the_cart()
        # удаление товара из корзины
        super().delete_product()
        # ОР
        title_basket = driver.find_element_by_xpath(locators.Basket['title_basket'])
        display = title_basket.is_displayed()
        print(display)
        # разлогин (постусловие)
        super().log_out()

    def Add_to_cart_check_delete_and_relogin(self):
        print("\n" + str(test_cases(5)))
        driver = self.driver
        # логин
        super().sing_in()
        # добавление товара в корзину
        super().add_product_to_cart()
        # ОР наличие товара в корзине
        super.check_the_item_in_the_cart()
        # удаление товара из корзины
        super().delete_product()
        # ОР
        title_basket = driver.find_element_by_xpath(locators.Basket['title_basket'])
        display = title_basket.is_displayed()
        print(display)
        # разлогин
        super().log_out()
        # ожидание
        time.sleep(60)
        # логин
        super().sing_in()
        # переход к корзине
        basket_button = driver.find_element_by_xpath(locators.Basket['basket_button'])
        basket_button.click()
        # ОР
        title_basket = driver.find_element_by_xpath(locators.Basket['title_basket'])
        display = title_basket.is_displayed()
        print(display)
        # постусловие разлогин
        super().log_out()

    def test_run(self):
        self.setUp()
        self.Wrong_and_correct_login()
        self.Add_to_cart()
        self.Add_to_cart_and_check()
        self.Add_to_cart_check_and_delete()
        self.Add_to_cart_check_delete_and_relogin()






    def tearDown(self):  # перенести в базовые ТК
        self.driver.quit()




if __name__ == '__main__':
    unittest.main()





