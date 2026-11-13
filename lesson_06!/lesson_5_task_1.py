from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()
    try:
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

        start_button = driver.find_element(By.CSS_SELECTOR, "#start button")
        start_button.click()

        hello_world_text = WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, 'finish'), "Hello World!")
        )

        screenshot_path = "./screenshot.png"
        driver.save_screenshot(screenshot_path)

        assert hello_world_text == True, f"Текст не найден или неверный."

    finally:
        driver.quit()
