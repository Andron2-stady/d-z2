from selenium.webdriver.common.by import By

class MainPage:
    ADD_TO_CART_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    # ... локаторы для других кнопок
    SHOPPING_CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver

    def add_backpack_to_cart(self):
        self.driver.find_element(*self.ADD_TO_CART_BACKPACK).click()

    # ... методы для добавления Bolt T-Shirt и Onesie

    def go_to_cart(self):
        self.driver.find_element(*self.SHOPPING_CART_LINK).click()
