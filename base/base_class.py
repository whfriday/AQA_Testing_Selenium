import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Base:
    """Базовый класс, содержащий универсальные методы"""

    def __init__(self, driver):
        self.driver = driver


    def get_current_url(self):
        """Method get current URL"""

        get_url = self.driver.current_url
        print(f'Current URL: {get_url}')


    def assert_word(self, word, result):
        """Method assert word"""

        value_word = word.text
        assert value_word == result
        print('Good value word')

    
    def get_screenshot(self):
        """Method do Screenshot"""

        now_date = datetime.datetime.now().strftime("%d.%m.%Y.%H.%M.%S")   
        name_screenshot = "screenshot " + now_date + ".png"     
        self.driver.save_screenshot(r"D:\\Python_Projects\\Vitaminoff_AQA_Project\\screen\\" + name_screenshot) 
        #путь к папке screen, в которую будут сохраняться скриншоты

    
    def assert_url(self, result):
        """Method assert URL"""

        get_url = self.driver.current_url
        assert get_url == result
        print('Good value url')

    
    