"""Написать тест с использованием pytest и requests, в котором:
Адрес сайта, имя пользователя и пароль хранятся в config.yaml
conftest.py содержит фикстуру авторизации по адресу 
https://test-stand.gb.ru/gateway/login с передачей параметров “username" и "password" 
и возвращающей токен авторизации
Тест с использованием DDT проверяет наличие поста 
с определенным заголовком в списке постов другого пользователя, для этого выполняется
 get запрос по адресу https://test-stand.gb.ru/api/posts c хедером, содержащим токен 
 авторизации в параметре "X-Auth-Token". Для отображения постов другого пользователя 
 передается "owner": "notMe"."""
import requests

responce = requests.post(url="https://test-stand.gb.ru/gateway/login",
                         data={"username": "GB202307c17509", "password": "89578a2581"})
print(responce.status_code)
print(responce.json()['token'])
