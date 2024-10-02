import sys
sys.path.append("D:\\Python_Projects\\Vitaminoff_AQA_Project") 
# Путь к директории проекта

from utilites.logger import Logger
from base.base_class import Base
from pages.product_page import Product_page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class Cart_page(Base):

    #Locators
    cart_clear_button = '//div[@class="basket-clear-button"]'
    product_title = '(//div[@class="basket-item-description-title"])[1]'
    total_price = '//div[@class="basket-coupon-block-total-price-current"]'
    checkout_button = '//button[@data-entity="basket-checkout-button"]'


    #Getters
    def get_cart_clear_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_clear_button)))
    
    def get_product_title(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_title)))
    
    def get_total_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.total_price)))
    
    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))
    
    
    #Actions
    def get_flavour(self):
        """Получение списка вкусов(4) товара из добавленных в корзину"""

        Cart_page.flavour = []
        for i in range(1, 5):
            driver = self.driver


            # Locators
            flavour_product = f'(//div[@class="basket-item-property-value"])[{i}]'


            # Getters
            def get_flavour_product():
                return WebDriverWait(driver, 30).until(
                    EC.element_to_be_clickable((By.XPATH, flavour_product))
                )


            # Actions
            def get_flavour_product_values():
                k = get_flavour_product().text
                Cart_page.flavour.append(k)
                return Cart_page.flavour

            get_flavour_product()
            get_flavour_product_values()
        

    def click_cart_clear_button(self):
        self.get_cart_clear_button().click()
        print('Click Clear cart')
        
    def assert_product_title_value(self):
        """Сверка наименования товара на его странице и в корзине"""

        Cart_page.product_title_value = self.get_product_title().text
        assert Product_page.product_title_value == Cart_page.product_title_value
        print("Product Name - Correct")

    def assert_total_price(self):
        """Сверка цены товара на его странице и в корзине"""

        Product_page.product_price_value = Product_page.product_price_value[:-1]
        Cart_page.total_price_value = self.get_total_price().text.replace(" ", "")
        Cart_page.total_price_value = Cart_page.total_price_value[:-1]
        assert int(Product_page.product_price_value) * 4 == int(Cart_page.total_price_value)
        print("Total Price - Correct")

    def assert_flavours(self):
        """Сверка вкусов товара на его странице и среди добавленных в корзину"""

        assert Product_page.flavour == Cart_page.flavour
        print('Flavours - Correct')

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print('Click Checkout')


    #Methods
    def clear_cart(self):
        """Очистка корзины"""

        self.get_current_url()
        self.get_screenshot()
        self.click_cart_clear_button()
        
    def check_cart_to_order(self):
        """Проверка корзины и переход к оформлению заказа"""
        with allure.step("Check cart to order"):

            Logger.add_start_step(method="check_cart_to_order")
            self.get_current_url()
            self.get_screenshot()
            self.assert_product_title_value()
            self.get_flavour()
            self.assert_flavours()
            self.assert_total_price()
            self.click_checkout_button()
            Logger.add_end_step(url=self.driver.current_url, method="check_cart_to_order")
