import pytest
from selenium import webdriver
from pages.calculator_page import CalculatorPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_slow_calculator(driver):
    page = CalculatorPage(driver)
    page.open()
    page.set_delay(45)

    page.click_number(7)
    page.click_operator("+")
    page.click_number(8)
    page.click_equals()
    result = page.get_result()
    assert result == "15"
