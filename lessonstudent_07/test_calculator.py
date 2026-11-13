import pytest
from selenium import webdriver
from pages.calculator_page import CalculatorPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_calculator_addition(driver):
    page = CalculatorPage(driver)
    page.open("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    page.set_delay(45)
    page.click_7()
    page.click_plus()
    page.click_8()
    page.click_equals()

    result = page.get_result()
    assert result == "15"
