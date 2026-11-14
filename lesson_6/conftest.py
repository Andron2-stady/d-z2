import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    # Драйвер будет создаваться по очереди для каждого браузера
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        # Добавим опцию headless(без запуска браузера)
        # options.add_argument("--headless")
        driver = webdriver.Chrome(
            service=ChromeDriverManager().install(), options=options)
    elif request.param == "firefox":
        options = webdriver.FirefoxOptions()
        # options.add_argument("--headless")
        driver = webdriver.Firefox(
            service=GeckoDriverManager().install(), options=options)

    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()  # Обязательно закрываем браузер после теста
