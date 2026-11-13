import pytest
from client import YougileClient
import uuid

client = YougileClient()

# Вспомогательная функция для генерации уникальных имен
def generate_unique_name(prefix="test"):
    return f"{prefix}_{uuid.uuid4().hex[:8]}"

# --- [POST] /api-v2/projects ---

def test_create_project_positive():
    project_name = generate_unique_name("pos")
    response = client.create_project(name=project_name)

    assert response.status_code == 200, f"Expected 200, got {
        response.status_code}"
    data = response.json()
    assert data["name"] == project_name

    # Очистка (Teardown)
    client.delete_project(data["id"])

def test_create_project_negative_empty_name():
    response = client.create_project(name="")
    assert response.status_code == 400
    # Yougile обычно возвращает сообщение об ошибке в поле 'message' или 'error'
    assert "message" in response.json() or "error" in response.json()

# --- [PUT] /api-v2/projects/{id} ---

def test_update_project_positive():
    # Arrange: создаем проект для теста
    project_name = generate_unique_name("upd")
    create_resp = client.create_project(name=project_name)
    project_id = create_resp.json()["id"]

    # Act
    new_name = project_name + "_updated"
    response = client.update_project(project_id=project_id, name=new_name)

    # Assert
    assert response.status_code == 200
    assert response.json()["name"] == new_name

    # Cleanup
    client.delete_project(project_id)

def test_update_project_negative_wrong_id():
    fake_id = "proj_000000000000000000000000"
    response = client.update_project(project_id=fake_id, name="test")
    assert response.status_code == 404

# --- [GET] /api-v2/projects/{id} ---

def test_get_project_positive():
    # Arrange
    project_name = generate_unique_name("get")
    create_resp = client.create_project(name=project_name)
    project_id = create_resp.json()["id"]

    # Act
    response = client.get_project(project_id=project_id)

    # Assert
    assert response.status_code == 200
    assert response.json()["name"] == project_name

    # Cleanup
    client.delete_project(project_id)

def test_get_project_negative_not_found():
    fake_id = "proj_111111111111111111111111"
    response = client.get_project(project_id=fake_id)
    assert response.status_code == 404

# метод удаления добавляется:
# def delete_project(self, project_id: str):
#     url = f"{BASE_URL}/api-v2/projects/{project_id}"
#     return self.session.delete(url)
