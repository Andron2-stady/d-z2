import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("YOUGILE_BASE_URL")
API_KEY = os.getenv("YOUGILE_API_KEY")
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

class YougileClient:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(HEADERS)

    def create_project(self, name: str, description: str = ""):
        url = f"{BASE_URL}/api-v2/projects"
        payload = {"name": name, "description": description}
        return self.session.post(url, json=payload)

    def update_project(self, project_id: str, name: str = None, description: str = None):
        url = f"{BASE_URL}/api-v2/projects/{project_id}"
        payload = {}
        if name:
            payload["name"] = name
        if description:
            payload["description"] = description
        return self.session.put(url, json=payload)

    def get_project(self, project_id: str):
        url = f"{BASE_URL}/api-v2/projects/{project_id}"
        return self.session.get(url)
