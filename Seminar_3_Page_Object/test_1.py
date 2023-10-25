from testpage import OperationsHelper
import logging
import yaml

with open("Seminar_3_Page_Object/testdata.yaml", encoding="utf-8") as f:
    testdata = yaml.safe_load(f)

def test_step1(browser):
    logging.info("Test1 Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == "401"

def test_step2(browser):
    logging.info("Test2 Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata.get("login"))
    testpage.enter_pass(testdata.get("passwd"))
    testpage.click_login_button()
    assert "hello" in testpage.get_text().lower(), "test FAILED"

# ДЗ-3. Добавить в проект тест по проверке механики работы формы Contact Us на главной странице личного кабинета. 
# Должно проверятся открытие формы, ввод данных в поля, клик по кнопке и появление всплывающего alert.
# Совет: переключиться на alert можно командой alert = self.driver.switch_to.alert
# Вывести текст alert.text
def test_step3(browser):
    logging.info("Test3 Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata.get("login"))
    testpage.enter_pass(testdata.get("passwd"))
    testpage.click_login_button()
    testpage.click_contact_button()
    testpage.enter_name(testdata.get("name"))
    testpage.enter_email(testdata.get("email"))
    testpage.enter_content(testdata.get("content"))
    testpage.click_contact_us_button()
    assert testpage.get_alert_message() == "Form successfully submitted", "test FAILED"