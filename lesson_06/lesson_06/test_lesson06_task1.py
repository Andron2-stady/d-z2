from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    """
    Тест проверяет динамическую загрузку контента.
    1. Открывает страницу с индикатором загрузки.
    2. Нажимает кнопку Start.
    3. Ожидает появления текста "Hello World!".
    4. Делает скриншот и проверяет текст.
    """
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

        start_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#start button"))
        )
        start_button.click()

        hello_text = wait.until(
            EC.visibility_of_element_located((By.ID, "finish"))
        )
        driver.save_screenshot("screenshot_task1.png")

        assert hello_text.text == "Hello World!", f"Ожидался текст 'Hello World!', но получено '{hello_text.text}'"

    finally:
        driver.quit()


if __name__ == "__main__":
    test_dynamic_loading()
