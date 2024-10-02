import sys
sys.path.append("D:\\Python_Projects\\Vitaminoff_AQA_Project")
# Путь к директории проекта

from utilites.logger import Logger
from pages.geyners_page import Gayners_page
from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import allure


class Product_page(Base):

    # Locators
    product_title = '//div[@class="product-description-name"]'
    product_price = '(//span[@class="price "])[1]'
    cart_button = '//a[@class="basket-block-link basket"]'


    # Getters
    def get_cart_button(self):
        return self.driver.find_element(By.XPATH, self.cart_button)

    def get_product_title(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.product_title))
        )

    def get_product_price(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.product_price))
        )


    # Actions
    def get_flavour(self):
        """Получение списка доступных вкусов(4) товара с его страницы"""

        Product_page.flavour = []
        for i in range(1, 5):
            driver = self.driver

            # Locators
            flavour_product = f'(//div[@class="option-item-title"])[{i}]'


            # Getters
            def get_flavour_product():
                return WebDriverWait(driver, 30).until(
                    EC.element_to_be_clickable((By.XPATH, flavour_product))
                )


            # Actions
            def get_flavour_product_values():
                k = get_flavour_product().text
                Product_page.flavour.append(k)
                return Product_page.flavour

            get_flavour_product()
            get_flavour_product_values()

    def add_products_to_cart(self):
        """Добавление всех доступных вкусов(4) в корзину"""

        for i in range(1, 5):
            driver = self.driver

            # Locators
            add_to_cart_button = f'(//button[@class="to-cart button"])[{i}]'


            # Getters
            def get_add_to_cart_button():
                return WebDriverWait(driver, 30).until(
                    EC.element_to_be_clickable((By.XPATH, add_to_cart_button))
                )


            # Actions
            def click_add_to_cart_button():
                get_add_to_cart_button().click()
                print(f"Click Add to cart #{i}")

            get_add_to_cart_button()
            click_add_to_cart_button()

    def move_to_cart_button(self):
        self.driver.execute_script("window.scrollBy(0, -500)")

    def click_cart_button(self):
        self.get_cart_button().click()
        print("Click Cart button")

    def assert_product_title(self):
        """Сверка наименования товара в каталоге и на его странице"""

        Product_page.product_title_value = self.get_product_title().text
        assert Gayners_page.product_title_value == Product_page.product_title_value
        print("Product Name - Correct")

    def assert_product_price(self):
        """Сверка цены товара в каталоге и на его странице"""

        Product_page.product_price_value = self.get_product_price().text.replace(" ", "")
        assert Gayners_page.product_price_value == Product_page.product_price_value
        print("Product Price - Correct")


    # Methods
    def checkout_products_to_cart(self):
        """Сверка и добавление товаров в корзину"""
        with allure.step("Checkout products to cart"):

            Logger.add_start_step(method="checkout_products_to_cart")
            self.get_current_url()
            self.assert_product_title()
            self.assert_product_price()
            self.get_flavour()
            self.add_products_to_cart()
            self.move_to_cart_button()
            self.click_cart_button()
            Logger.add_end_step(url=self.driver.current_url, method="checkout_products_to_cart")
