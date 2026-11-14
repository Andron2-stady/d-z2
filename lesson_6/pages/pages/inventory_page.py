from selenium.webdriver.common.by import By


class InventoryPage:
    ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    ADD_BOLT_TSHIRT = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ADD_ONESIE = (By.ID, "add-to-cart-sauce-labs-onesie")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver

    def add_backpack(self):
        self.driver.find_element(*self.ADD_BACKPACK).click()

    def add_bolt_tshirt(self):
        self.driver.find_element(*self.ADD_BOLT_TSHIRT).click()

    def add_onesie(self):
        self.driver.find_element(*self.ADD_ONESIE).click()

    def go_to_cart(self):
        self.driver.find_element(*self.CART_LINK).click()
