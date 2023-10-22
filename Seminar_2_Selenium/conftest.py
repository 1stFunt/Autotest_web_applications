import yaml
from module import Site
import pytest

with open("Seminar_2_Selenium/testdata.yaml", encoding="utf-8") as f:
    testdata = yaml.safe_load(f)


@pytest.fixture()
def selector_login():
    return """//*[@id="login"]/div[1]/label/input"""


@pytest.fixture()
def selector_passwd():
    return """//*[@id="login"]/div[2]/label/input"""


@pytest.fixture()
def selector_button():
    return "button"


@pytest.fixture()
def selector_error():
    return """//*[@id="app"]/main/div/div/div[2]/h2"""


@pytest.fixture()
def selector_home():
    return """//*[@id="app"]/main/nav/a/span"""


@pytest.fixture()
def site():
    site_inst = Site(testdata["address"])
    yield site_inst
    site_inst.my_quit()


# ДЗ-2
@pytest.fixture()
def add_post_selector():
    return """//*[@id="create-btn"]"""


@pytest.fixture()
def add_title():
    return """//*[@id="create-item"]/div/div/div[1]/div/label/input"""


@pytest.fixture()
def add_description():
    return """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea"""


@pytest.fixture()
def add_content():
    return """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea"""


@pytest.fixture()
def save_post():
    return """//*[@id="create-item"]/div/div/div[7]/div/button"""


@pytest.fixture()
def check_title():
    return """//*[@id="app"]/main/div/div[1]/h1"""


@pytest.fixture()
def title_name():
    return f"{testdata['title']}"
