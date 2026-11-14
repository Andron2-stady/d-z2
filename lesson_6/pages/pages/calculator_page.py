from selenium.webdriver.common.by import By


class CalculatorPage:
    DELAY_INPUT = (By.ID, "delay")
    BUTTON_7 = (By.XPATH, "//button[text()='7']")
    BUTTON_PLUS = (By.XPATH, "//button[text()='+']")
    BUTTON_8 = (By.XPATH, "//button[text()='8']")
    BUTTON_EQUALS = (By.XPATH, "//button[text()='=']")
    RESULT_DISPLAY = (By.ID, "display")

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        """Открыть страницу калькулятора"""
        self.driver.get(url)

    def set_delay(self, seconds: int):
        """Установить задержку вычислений"""
        delay_field = self.driver.find_element(*self.DELAY_INPUT)
        delay_field.clear()
        delay_field.send_keys(str(seconds))

    def click_button(self, digit: str):
        """
        Нажать кнопку цифры или оператора.
        :param digit: Символ кнопки ('0'–'9', '.', '+', '-', '*', '/', '=').
        """

        button = self.driver.find_element(
            By.CSS_SELECTOR, f"[value='{digit}']")
        button.click()

    def get_result(self) -> str:
        """Вернуть текущее значение дисплея калькулятора"""
        return self.driver.find_element(*self.RESULT_DISPLAY).text.strip()
