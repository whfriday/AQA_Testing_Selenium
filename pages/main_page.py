import os
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Путь к директории проекта

import sys
sys.path.append(project_dir) 
# Путь для импорта файлов проекта

from utilites.logger import Logger
from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class Main_page(Base):

    #Locators
    menu_button = '//a[@id="menu-button"]'
    sportpit_section = '(//a[@class="nav-icon"])[2]'
    gayner_section = '(//a[@href="/catalog/geynery/"])[2]'
    header = '//div[@class="__line-blocks _content-justify _items-center"]/h1'


    #Getters
    def get_menu_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu_button)))
    
    def get_sportpit_section(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sportpit_section)))

    def get_gayner_section(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.gayner_section)))
    
    def get_header(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.header)))
    

    #Actions
    def click_menu_button(self):
        self.get_menu_button().click()
        print('Click Menu')

    def click_sportpit_section(self):
        self.get_sportpit_section().click()
        print('Click Sportpit')

    def click_gayner_section(self):
        self.get_gayner_section().click()
        print('Click Gayners')


    #Methods
    def go_shoping_page(self):
        """Переход в каталог товаров(гейнеры)"""
        with allure.step("Go shopping page"):

            Logger.add_start_step(method="go_shoping_page")
            self.click_menu_button()
            self.click_sportpit_section()
            self.click_gayner_section()
            self.assert_word(self.get_header(), "Гейнеры")
            self.get_current_url()
            Logger.add_end_step(url=self.driver.current_url, method="go_shoping_page")