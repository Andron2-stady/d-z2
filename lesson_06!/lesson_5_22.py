from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # Открываем главную страницу, чтобы задать домен
        driver.get("https://gitflic.ru/")

        # --- Пользователь 1 ---
        user1_cookies = [
            {'name': 'access_token','SESSION' 'X-CSRF-TOKEN' 'value':'a41ba4db-b33b-42a9-ae3e-4c2363bba64e', }
        ]

        for cookie in user1_cookies:
            driver.add_cookie(cookie)

        # Обновить страницу
        driver.refresh()

        # Перейти на страницу пользователя 1
        driver.get("https://gitflic.ru/user/")

        # Сохранить текущий URL
        user1_url = driver.current_url

        # (очистить куки)
        driver.delete_all_cookies()

        # Снова открыть главную страницу
        driver.get("https://gitflic.ru/")

        # --- Пользователь 2 ---
        # Установить cookie пользователя 2 
        user2_cookies = [
            {'name': 'access_token', 'X-CSRF-TOKEN' 'value': '2d93ea35-05e5-41f1-96f6-6aace8c80875'},
        ]

        for cookie in user2_cookies:
            driver.add_cookie(cookie)

        driver.refresh()

        # Перейти на страницу пользователя 2
        driver.get("https://gitflic.ru/user/import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def test_session_storage_auth():
    options = Options()
    # Добавляем опцию headless=False, чтобы видеть работу браузера.

    service = Service()  # Для Selenium 4.x
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # Предварительные шаги: загрузили данные пользователей.
        with open("./user1_cookies.json", encoding='utf-8') as file:
            user1_data = json.load(file)
        with open("./user2_cookies.json", encoding='utf-8') as file:
            user2_data = json.load(file)

        # cookie пользователя 1.
        driver.get("https://gitflic.ru/")
        for cookie in user1_data:
            if cookie["domain"] != "":
                driver.add_cookie(cookie)

        # Обновите страницу.
        driver.refresh()

        # Перейдите на страницу пользователя 1.
        url_user1_profile = "https://gitflic.ru/profile/user1_username/"
        driver.get(url_user1_profile)
        profile_url_1 = driver.current_url

        # Разлогиньтесь (очистите куки).
        driver.delete_all_cookies()

        # Установим cookie пользователя 2.
        driver.get("https://gitflic.ru/")
        for cookie in user2_data:
            if cookie["domain"] != "":
                driver.add_cookie(cookie)

        # Обновите страницу.
        driver.refresh()

        # Перейдите на страницу пользователя 2.
        url_user2_profile = "https://gitflic.ru/profile/user2_username/"
        driver.get(url_user2_profile)
        profile_url_2 = driver.current_url

        # Проверено, что URL профилей различаются.
        assert profile_url_1 != profile_url_2, \
            f"URL профилей совпадают:\n{profile_url_1}\n{profile_url_2}"

    finally:
        driver.quit())

        user2_url = driver.current_url

        # Проверить, что URL для пользователя 1 и пользователя 2 различаются
        assert user1_url != user2_url,
        f"URL пользователей совпадают: {user1_url}"

    finally:
        driver.quit()


if __name__ == "__main__":
    test_session_storage_auth()
