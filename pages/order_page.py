import sys
sys.path.append("D:\\Python_Projects\\Vitaminoff_AQA_Project") 
# Путь к директории проекта

from utilites.logger import Logger
import datetime
from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
import allure


class Order_page(Base):

    #Locators
    metro_station_field = '(//div[@class="form-group bx-soa-customer-field"])[5]'
    botanich_sad = '//*[@id="bx-soa-properties"]/div[2]/div[2]/div[1]/div[7]/div/select/option[27]'
    adress_field = '//input[@id="soa-property-23"]'
    date_field = '//input[@id="soa-property-24"]'
    card_pay = '//div[contains(text(),"Онлайн оплата")]'

    #Getters

    def get_metro_station_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.metro_station_field)))
    
    def get_adress_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.adress_field)))
    
    def get_date_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.date_field)))
    
    def get_botanich_sad(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.botanich_sad)))
    
    def get_card_pay(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.card_pay)))
    
    #Actions

    def click_metro_station_field(self):
        self.get_metro_station_field().click()
        print('Click metro station')
        
    def click_botanich_sad(self):
        self.get_botanich_sad().click()
        print('Click Botanich Sad')
    
    def click_adress_field(self):
        self.get_adress_field().click()
        print('Click Adress')

    def input_adress(self):
        self.get_adress_field().send_keys('Лазоревый проезд, 1, Москва')
        print('Input Adress')

    def input_date(self):
        current_date = datetime.datetime.today()   
        future_date = current_date + datetime.timedelta(days=1)    
        future_date = datetime.datetime.strftime(future_date, '%d.%m.%y')
        self.get_date_field().send_keys(future_date)
        self.get_date_field().send_keys(Keys.ENTER)

    def click_card_pay(self):
        self.get_card_pay().click()
        print('Click Card')


    #Methods
    def confirm_order_info(self):
        """Заполнение полей оформления"""
        with allure.step("Confirm order info"):

            Logger.add_start_step(method="confirm_order_info")
            self.get_current_url()
            self.click_adress_field()
            self.input_adress()
            self.click_metro_station_field()
            self.click_botanich_sad()
            self.input_date()
            self.click_card_pay()
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method="confirm_order_info")
