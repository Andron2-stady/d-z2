import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_shop_checkout_flow(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    main_page = MainPage(driver)
    main_page.add_backpack_to_cart()
    main_page.add_bolt_tshirt_to_cart() # метод нужно добавить в класс
    main_page.add_onesie_to_cart()      # метод нужно добавить в класс
    
    main_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.click_checkout()

    checkout_page = CheckoutPage(driver)
    # Введите свои реальные данные
    checkout_page.fill_form("Ivan", "Ivanov", "123456")
    
    total_price = checkout_page.get_total_price()
    assert total_price == "Total: $58.29"
