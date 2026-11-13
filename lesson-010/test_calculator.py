import allure
import pytest
from selenium import webdriver
from pages.calculator_page import CalculatorPage

@allure.feature("Calculator")
@allure.story("Addition with delay")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Проверка сложения 7 + 8 на медленном калькуляторе")
@allure.description("""
    Тест проверяет корректность сложения чисел 7 и 8.
    Перед вводом данных устанавливается искусственная задержка работы.
""")
def test_calculator_addition():
    with allure.step("Инициализация драйвера Chrome"):
        driver = webdriver.Chrome()
        driver.maximize_window()

    try:
        page = CalculatorPage(driver)

        with allure.step("Открытие тестовой страницы"):
            page.open("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        with allure.step("Установка задержки 45 секунд"):
            page.set_delay(45)

        with allure.step("Выполнение арифметической операции 7 + 8"):
            page.click_7()
            page.click_plus()
            page.click_8()
            page.click_equals()

        with allure.step("Получение и проверка результата"):
            result = page.get_result()
            allure.attach(
                body=result,
                name="Result from page",
                attachment_type=allure.attachment_type.TEXT
            )
            assert result == "15", f"Ожидался результат 15, но получено {result}"

    finally:
        with allure.step("Закрытие браузера"):
            driver.quit()
