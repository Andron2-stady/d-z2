from selenium.webdriver.common.by import By

class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def add_backpack_to_cart(self):
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    def add_bolt_tshirt_to_cart(self):
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-tshirt").click()

    def add_onesie_to_cart(self):
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    def go_to_cart(self):
        self.driver.find_element(By.ID, "shopping_cart_container").click()
