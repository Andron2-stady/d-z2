from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/links/10")

    links = driver.find_elements(By.TAG_NAME, 'a')

    # Шаг 2: Проверяем количество ссылок
    assert len(links) == 9, f"Найдено {len(links)} ссылок вместо 9"

    # Шаг 3: Проверяем отображение всех ссылок
    for i, link in enumerate(links):
        assert link.is_displayed(), f"Ссылка #{i+1} скрыта!"

    # Шаг 4: Проверяем первую ссылку
    first_link_text = links[0].text.strip()
    assert '1' in first_link_text, \
        f"Текст первой ссылки '{first_link_text}' не содержит цифры 1."

    driver.quit()