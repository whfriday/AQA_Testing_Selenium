import sys
sys.path.append("D:\\Python_Projects\\Vitaminoff_AQA_Project")
# Путь к директории проекта

from utilites.logger import Logger
from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class Login_page(Base):

    #Variables
    url = 'https://vitaminof.ru/'
    email_value = 'jora.georg89@gmail.com'
    password_value = 'nU8SPwg8@n6aT4'
        
        
    #Locators
    lk_button = '//div[@class="header-item-personal"]'
    email = '//input[@name="USER_LOGIN"]'
    password = '//input[@name="USER_PASSWORD"]'
    login_button = '//button[@name="Login"]'
    notification = '//button[@id="onesignal-slidedown-cancel-button"]'
    

    #Getters
    def get_lk_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.lk_button)))
    
    def get_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))
    
    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))
    
    def get_notification(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.notification)))
    

    #Actions
    def click_lk_button(self):
        self.get_lk_button().click()
        print('Click LK')

    def input_email(self):
        self.get_email().send_keys(self.email_value)
        print('Input EMAIL')

    def input_password(self):
        self.get_password().send_keys(self.password_value)
        print('Input Password')
    
    def click_login_button(self):
        self.get_login_button().click()
        print('Click LOGIN')

    def close_notification(self):
        self.get_notification().click()
        print('Close Notification')


    #Methods
    def authorization(self):
        """Авторизация на сайте"""
        with allure.step("Authorization"):

            Logger.add_start_step(method="authorization")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.close_notification()
            self.click_lk_button()
            self.input_email()
            self.input_password()
            self.click_login_button()
            self.get_screenshot()
            self.get_current_url()
            Logger.add_end_step(url=self.driver.current_url, method="authorization")
            