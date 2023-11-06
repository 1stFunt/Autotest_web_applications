import pytest
import yaml
import requests
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

with open("testdata.yaml", encoding="utf-8") as f:
    testdata = yaml.safe_load(f)
    browser = testdata["browser"]


@pytest.fixture(scope="session")
def browser():
    if browser == "firefox":
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@pytest.fixture(scope="module", autouse=True)
def send_email():
    fromaddr = testdata.get("fromaddr")
    toaddr = testdata.get("toaddr")
    mypass = testdata.get("fromaddr_passwd")
    file = testdata.get("file")

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Привет от питона"

    with open(file, "rb") as fl:
        part = MIMEApplication(fl.read(), Name=basename(file))
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(
            file)
        msg.attach(part)

    letter = testdata.get("letter_body")

    msg.attach(MIMEText(letter, "plain"))
    # Создаем SMTP объект и настраиваем EHLO команду с указанием кодировки
    server = smtplib.SMTP_SSL("smtp.mail.ru", 465)
    server.ehlo('utf-8')  # Указываем кодировку для EHLO команды
    server.login(fromaddr, mypass)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()


@pytest.fixture()
def user_login():
    try:
        result = requests.Session().post(url=testdata['url'], data={'username': testdata['login'], 'password': testdata['passwd']})
        response_json = result.json()
        token = response_json.get('token')
    except:
        logging.exception("Get token exception")
        token = None
    logging.debug(f"Return token success")
    return token
