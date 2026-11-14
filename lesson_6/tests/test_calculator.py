import time
import pytest
from pages.calculator_page import CalculatorPage

URL_CALCULATOR = 'https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html'
DELAY_VALUE = 5  # Можно менять значение задержки для проверки

# Используем общую фикстуру из conftest.py
@pytest.mark.parametrize("browser_name", ["chrome", "firefox"], indirect=True)
def test_slow_calculator(driver, browser_name):
    page = CalculatorPage(driver)

    # Действие 1: Открываем страницу
    page.open(URL_CALCULATOR)

    # Действие 2: Устанавливаем задержку
    page.set_delay(DELAY_VALUE)

    # Действие 3: Нажимаем кнопки
    page.click_button('7')
    page.click_operator('+')
    page.click_button('8')
    page.click_equals()

    # Ждём результат с запасом
    time.sleep(DELAY_VALUE + 2)

    # Проверка результата
    result = page.get_result()
    assert result == '15',
    f"Результат {result} не равен ожидаемому значению 15"

