from selenium.webdriver.common.by import By


class CheckoutPage:
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    ZIP_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_AMOUNT = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver):
        self.driver = driver

    def fill_form(self, first_name, last_name, zip_code):
        self.driver.find_element(*self.FIRST_NAME).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
        self.driver.find_element(*self.ZIP_CODE).send_keys(zip_code)
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def get_total(self):
        return self.driver.find_element(*self.TOTAL_AMOUNT).text
