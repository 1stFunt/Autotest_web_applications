from login import get_post
import pytest
import requests
import yaml

with open("Seminar_1\REST\config.yaml", encoding="utf-8") as f:
    data = yaml.safe_load(f)


def test_step1(login):
    res = get_post(login)
    if res is None:
        raise Exception("Запрос вернул пустой результат")
    res_list = res.get("data")
    if res_list is None:
        raise Exception("Результат не содержит данных")
    res_id_list = [item['id'] for item in res_list]
    assert 1234 in res_id_list, "тест не пройден"

# ДЗ-1. Добавить в задание с REST API ещё один тест, в котором создаётся новый пост,
# а потом проверяется его наличие на сервере по полю «описание».
# Подсказка: создание поста выполняется запросом к https://test-stand.gb.ru/api/posts
# с передачей параметров title, description, content.
def test_check_post_create(create_post, login):
    create_post
    token = login
    result = requests.Session().get(url=data['url_post'], headers={'X-Auth-Token': token}).json()['data']
    list_description = [i['description'] for i in result]
    assert data['description'] in list_description, 'check_post_create FAIL'


if __name__ == '__main__':
    pytest.main(["-vv"])
