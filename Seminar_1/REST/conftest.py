import pytest
import yaml
import requests

with open("Seminar_1\REST\config.yaml", encoding="utf-8") as f:
    data = yaml.safe_load(f)


@pytest.fixture()
def login():
    responce = requests.post(url=data.get("url_login"),
                             data={"username": data.get("username"), "password": data.get("password")})
    if responce.status_code == 200:
        return responce.json()['token']


@pytest.fixture()
def get_post(token):
    responce = requests.post(url=data.get("url_post"),
                             headers={"X-Auth-Token": token},
                             params={"owner": "notMe"})
    return responce.json()

# ДЗ -1
@pytest.fixture
def create_post(login):
    token = login

    def _create_post():
        post_data = {
            "title": data.get("title"),
            "description": data.get("description"),
            "content": data.get("content")
        }
        headers = {
            "X-Auth-Token": token
        }
        response = requests.post(data.get("url_post"),
                                 headers=headers, data=post_data)
        if response.status_code == 200:
            print("Пост успешно создан")
    return _create_post
