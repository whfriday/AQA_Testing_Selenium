import sys
sys.path.append("D:\\Python_Projects\\Automatization_Project")
# Путь к директории проекта


from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.geyners_page import Gayners_page
from pages.product_page import Product_page
from pages.cart_page import Cart_page
from pages.order_page import Order_page
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import allure



@allure.description("Test buy maxler")
def test_buy_maxler(set_up):
    """Тест по покупке 4шт гейнера бренда Maxler"""
    
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)

    lp = Login_page(driver)
    lp.authorization()  # Метод авторизации пользователя

    mp = Main_page(driver)
    mp.go_shoping_page()    # Переход в каталог

    gp = Gayners_page(driver)
    gp.filter_products()    # Фильтрация и выбор товара в каталоге

    pp = Product_page(driver)
    pp.checkout_products_to_cart()  # Сверка в карточке товара и добавление в корзину

    cp = Cart_page(driver)
    cp.check_cart_to_order()    # Сверка в корзине и переход к оформлению заказа

    op = Order_page(driver)
    op.confirm_order_info()     # Заполнение полей оформления

    driver.quit()
