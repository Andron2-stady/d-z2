from typing import Any
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class MainPage:
    """Класс главной страницы магазина."""
    ADD_TO_CART_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    ADD_TO_CART_BOLT = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ADD_TO_CART_ONESIE = (By.ID, "add-to-cart-sauce-labs-onesie")
    SHOPPING_CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def add_backpack_to_cart(self) -> None:
        """Добавляет рюкзак в корзину."""
        self.driver.find_element(*self.ADD_TO_CART_BACKPACK).click()

    def add_bolt_tshirt_to_cart(self) -> None:
        """Добавляет футболку Bolt в корзину."""
        self.driver.find_element(*self.ADD_TO_CART_BOLT).click()

    def add_onesie_to_cart(self) -> None:
        """Добавляет комбинезон Onesie в корзину."""
        self.driver.find_element(*self.ADD_TO_CART_ONESIE).click()

    def go_to_cart(self) -> None:
        """Переходит в корзину."""
        self.driver.find_element(*self.SHOPPING_CART_LINK).click()
