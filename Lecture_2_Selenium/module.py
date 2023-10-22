import yaml
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager 

with open("Lecture_2_Selenium/testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    browser = testdata["browser"]
# service = Service(testdata["driver_path"])
# options = webdriver.ChromeOptions()


class Site:
    def __init__(self, address):
        if browser == "chrome":
            service = Service(executable_path=ChromeDriverManager().install())
            options = webdriver.ChromeOptions()
            self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.implicitly_wait(5)    
        self.driver.maximize_window()
        self.driver.get(address)
        time.sleep(testdata["sleep_time"])

    def find_element(self, mode, path):
        if mode == "css":
            element = self.driver.find_element(By.CSS_SELECTOR, path)
        elif mode == "xpath":
            element = self.driver.find_element(By.XPATH, path)
        else:
            element = None
        return element

    def get_element_property(self, mode, path, property):
        element = self.find_element(mode, path)
        return element.value_of_css_property(property)

    def close(self):
        self.driver.close()

# Вместо time:
# from selenium import webdriver
# driver = webdriver.Chrome
# driver.implicitly_wait(10)
# driver.get("https://test-stand.gb.ru/")
# myDynamicElement = driver.find_element_by_id("myDynamicElement")