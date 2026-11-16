from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 60)

    def open(self):
        self.driver.get(self.URL)

    def set_delay(self, seconds):
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(str(seconds))

    def click_number(self, number):
        self.driver.find_element(By.ID, f"num-{number}").click()

    def click_operator(self, operator):
        self.driver.find_element(By.ID, f"op-{operator}").click()

    def click_equals(self):
        self.driver.find_element(By.ID, "eq").click()

    def get_result(self):
        # Ожидаем появления результата, так как калькулятор "медленный"
        result_element = self.wait.until(EC.visibility_of_element_located((By.ID, "result")))
        return result_element.text
