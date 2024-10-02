import sys
sys.path.append("D:\\Python_Projects\\Vitaminoff_AQA_Project")
# Путь к директории проекта

from utilites.logger import Logger
from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class Gayners_page(Base):

    # Locators
    show_all_brands = '(//div[@class="show-overflow"])[2]'
    maxler_checkbox = '//*[@id="overflow-container-brand"]/label[7]'
    confirm_button = '//a[@class="button white_bg"]'
    min_price = '//input[@id="MSHOP_SMART_FILTER_P1_MIN"]'
    max_price = '//input[@id="MSHOP_SMART_FILTER_P1_MAX"]'
    product = '//a[@class="product-item-link"]'
    product_title = '//div[@class="product-item-title"]'
    product_price = '//div[@class="item-sell-price"]'


    # Getters
    def get_show_all_brands(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.show_all_brands))
        )

    def get_maxler_checkbox(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.maxler_checkbox))
        )

    def get_confirm_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.confirm_button))
        )

    def get_min_price(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.min_price))
        )

    def get_max_price(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.max_price))
        )

    def get_product(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.product))
        )

    def get_product_title(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.product_title))
        )

    def get_product_price(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.product_price))
        )


    # Actions
    def click_show_all_brands(self):
        self.get_show_all_brands().click()
        print("Click All Brands")

    def click_maxler_checkbox(self):
        self.get_maxler_checkbox().click()
        print("Click Maxler Brand")

    def click_confirm_button(self):
        self.get_confirm_button().click()
        print("Click Confirm")

    def input_min_price(self):
        self.get_min_price().send_keys("4000")
        print("Input min price")

    def input_max_price(self):
        self.get_max_price().send_keys("7000")
        print("Input max price")

    def click_product(self):
        self.get_product().click()
        print("Click Product link")

    def get_product_title_price_value(self):
        """Получение наименования и цены товара"""

        Gayners_page.product_title_value = self.get_product_title().text
        Gayners_page.product_price_value = self.get_product_price().text.replace(' ', '')
        return Gayners_page.product_title_value, Gayners_page.product_price_value
    

    # Methods
    def filter_products(self):
        """Сортировка фильтрами и переход в карточку товара"""
        with allure.step("Filter products"):

            Logger.add_start_step(method="filter_products")
            self.click_show_all_brands()
            self.click_maxler_checkbox()
            self.click_confirm_button()
            self.get_screenshot()
            self.input_min_price()
            self.input_max_price()
            self.click_confirm_button()
            self.get_screenshot()
            self.get_current_url()
            self.get_product_title_price_value()
            self.click_product()
            Logger.add_end_step(url=self.driver.current_url, method="filter_products")