import yaml
# from module import Site
import pytest
import time

with open("Seminar_2_Selenium/testdata.yaml", encoding="utf-8") as f:
    testdata = yaml.safe_load(f)
# site = Site(testdata["address"])

def test_step1(site, selector_login, selector_passwd, selector_button, selector_error):
    input1 = site.find_element("xpath", selector_login)
    input1.send_keys("test")
    input2 = site.find_element("xpath", selector_passwd)
    input2.send_keys("test")
    btn = site.find_element("css", selector_button)
    btn.click()
    err_text3 =site.find_element("xpath", selector_error)
    assert err_text3.text == "401"

def test_step2(site, selector_login, selector_passwd, selector_button, selector_home):
    input1 = site.find_element("xpath", selector_login)
    input1.send_keys(testdata.get("username"))
    input2 = site.find_element("xpath", selector_passwd)
    input2.send_keys(testdata.get("password"))
    btn = site.find_element("css", selector_button)
    btn.click()
    home_path = site.find_element("xpath", selector_home)
    assert home_path.text == "Home", "test FAIL"

# ДЗ-2. Добавить в наш тестовый проект шаг добавления поста после входа. 
# Должна выполняться проверка на наличие названия поста на странице сразу после его создания.
# Совет: не забудьте добавить небольшие ожидания перед и после нажатия кнопки создания поста.
def test_add_post(site, selector_login, selector_passwd, selector_button, add_post_selector, add_title, add_description,
                  add_content, save_post, check_title, title_name):
    input1 = site.find_element("xpath", selector_login)
    input1.clear()
    input1.send_keys(testdata["username"])
    input2 = site.find_element("xpath", selector_passwd)
    input2.clear()
    input2.send_keys(testdata["password"])
    btn = site.find_element("css", selector_button)
    btn.click()
    time.sleep(testdata["sleep_time"])
    btn = site.find_element("xpath", add_post_selector)
    btn.click()
    input3 = site.find_element("xpath", add_title)
    input3.clear()
    input3.send_keys(testdata["title"])
    input4 = site.find_element("xpath", add_description)
    input4.clear()
    input4.send_keys(testdata["description"])
    input5 = site.find_element("xpath", add_content)
    input5.clear()
    input5.send_keys(testdata["content"])
    btn = site.find_element("xpath", save_post)
    btn.click()
    time.sleep(testdata["sleep_time"])
    code_label = site.find_element("xpath", check_title).text
    assert code_label == title_name, "test FAIL"
    site.driver.close()


if __name__ == "__main__":
    pytest.main(["-vv"])