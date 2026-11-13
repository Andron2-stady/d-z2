from typing import Any
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    """Класс страницы медленного калькулятора."""
    DELAY_INPUT = (By.ID, "delay")
    BUTTON_7 = (By.XPATH, "//button[text()='7']")
    BUTTON_PLUS = (By.XPATH, "//button[text()='+']")
    BUTTON_8 = (By.XPATH, "//button[text()='8']")
    BUTTON_EQUALS = (By.XPATH, "//button[text()='=']")
    RESULT = (By.ID, "answer")

    def __init__(self, driver: WebDriver):
        """
        Инициализация страницы.

        :param driver: Экземпляр Selenium WebDriver.
        """
        self.driver = driver

    def open(self, url: str) -> None:
        """
        Открывает страницу по URL.

        :param url: Адрес страницы.
        """
        self.driver.get(url)

    def set_delay(self, seconds: int) -> None:
        """
        Устанавливает задержку работы калькулятора.

        :param seconds: Время задержки в секундах.
        """
        delay_field = self.driver.find_element(*self.DELAY_INPUT)
        delay_field.clear()
        delay_field.send_keys(str(seconds))

    def click_7(self) -> None:
        """Нажимает кнопку '7'."""
        self.driver.find_element(*self.BUTTON_7).click()

    def click_plus(self) -> None:
        """Нажимает кнопку '+'."""
        self.driver.find_element(*self.BUTTON_PLUS).click()

    def click_8(self) -> None:
        """Нажимает кнопку '8'."""
        self.driver.find_element(*self.BUTTON_8).click()

    def click_equals(self) -> None:
        """Нажимает кнопку '='."""
        self.driver.find_element(*self.BUTTON_EQUALS).click()

    def get_result(self) -> str:
        """
        Получает текст результата вычисления.

        :return: Текст из элемента с ответом.
        """
        element = WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located(self.RESULT)
        )
        return element.text
