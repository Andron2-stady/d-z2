from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


USER1_COOKIES = [
]

USER2_COOKIES = [
]


def setup_cookies_and_navigate(driver, cookies, target_path):
    """
    Устанавливает куки, обновляет страницу и переходит по целевому пути.
    """
    driver.get("https://gitflic.ru/")
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()
    driver.get(f"https://gitflic.ru{target_path}")


def test_session_storage_auth():
    """
    Тест проверяет авторизацию через установку cookie.
    Сравнивает URL профилей двух разных пользователей.
    """
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        if not USER1_COOKIES or not USER2_COOKIES:
            raise ValueError("Заполните списки USER1_COOKIES и USER2_COOKIES актуальными данными.")

        url_user1 = None
        url_user2 = None

        setup_cookies_and_navigate(driver, USER1_COOKIES, "/user1_username")
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".profile-header__username")))
        url_user1 = driver.current_url

        driver.delete_all_cookies()

        setup_cookies_and_navigate(driver, USER2_COOKIES, "/user2_username")
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".profile-header__username")))
        url_user2 = driver.current_url

        assert url_user1 != url_user2, f"URL пользователей совпали: {url_user1}"

    finally:
        driver.quit()


if __name__ == "__main__":
    test_session_storage_auth()