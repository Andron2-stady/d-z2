import allure
import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@allure.feature("SauceDemo Shop")
@allure.story("Checkout flow")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Проверка оформления заказа в интернет-магазине")
@allure.description("""
    Тест выполняет полный цикл покупки:
    авторизация -> добавление 3 товаров -> переход в корзину -> оформление заказа -> проверка итоговой суммы.
""")
def test_shop_checkout_flow():
    with allure.step("Инициализация драйвера Firefox"):
        driver = webdriver.Firefox()
        driver.maximize_window()

    try:
        login_page = LoginPage(driver)

        with allure.step("Открытие страницы авторизации"):
            login_page.open()

        with allure.step("Авторизация под стандартным пользователем"):
            login_page.login("standard_user", "secret_sauce")

        main_page = MainPage(driver)
        with allure.step("Добавление товаров в корзину"):
            main_page.add_backpack_to_cart()
            main_page.add_bolt_tshirt_to_cart()
            main_page.add_onesie_to_cart()

        with allure.step("Переход в корзину"):
            main_page.go_to_cart()

        cart_page = CartPage(driver)
        with allure.step("Переход к оформлению заказа"):
            cart_page.click_checkout()

        checkout_page = CheckoutPage(driver)
        with allure.step("Заполнение данных покупателя"):
            checkout_page.fill_form("Ivan", "Ivanov", "123456")

        with allure.step("Проверка итоговой стоимости заказа"):
            total_price = checkout_page.get_total_price()
            allure.attach(
                body=total_price,
                name="Total price",
                attachment_type=allure.attachment_type.TEXT
            )
            assert total_price == "Total: $58.29", f"Ожидалась сумма 58.29, но получено {total_price}"

    finally:
        with allure.step("Закрытие браузера"):
            driver.quit()
