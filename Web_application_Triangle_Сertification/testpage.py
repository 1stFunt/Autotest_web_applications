from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging


class TestSearchLocators:
    """
    Класс, содержащий локаторы элементов страницы, используемых для поиска элементов.
    """
    LOCATOR_SIDE1_FIELD = (
        By.XPATH, """/html/body/div[1]/div[3]/div[1]/form/input[1]""")
    LOCATOR_SIDE2_FIELD = (
        By.XPATH, """/html/body/div[1]/div[3]/div[1]/form/input[2]""")
    LOCATOR_SIDE3_FIELD = (
        By.XPATH, """/html/body/div[1]/div[3]/div[1]/form/input[3]""")
    LOCATOR_BUTTON = (By.CSS_SELECTOR, """#identify-triangle-action""")
    LOCATOR_TEXT_FIELD = (By.XPATH, """/html/body/div[1]/div[3]/div[2]""")


class OperationsHelper(BasePage):
    """
    Класс `OperationsHelper`, наследуется от класса `BasePage` и предоставляет методы 
    для выполнения операций на веб-странице, такие как ввод данных и нажатие кнопок.
    """

    def enter_side1(self, side):
        logging.info(
            f"Send {side} to element {TestSearchLocators.LOCATOR_SIDE1_FIELD[1]}")
        side_field = self.find_element(TestSearchLocators.LOCATOR_SIDE1_FIELD)
        side_field.clear()
        side_field.send_keys(side)

    def enter_side2(self, side):
        logging.info(
            f"Send {side} to element {TestSearchLocators.LOCATOR_SIDE2_FIELD[1]}")
        side_field = self.find_element(TestSearchLocators.LOCATOR_SIDE2_FIELD)
        side_field.clear()
        side_field.send_keys(side)

    def enter_side3(self, side):
        logging.info(
            f"Send {side} to element {TestSearchLocators.LOCATOR_SIDE3_FIELD[1]}")
        side_field = self.find_element(TestSearchLocators.LOCATOR_SIDE3_FIELD)
        side_field.clear()
        side_field.send_keys(side)

    def click_button(self):
        logging.info("Click button")
        self.find_element(TestSearchLocators.LOCATOR_BUTTON).click()

    def get_text(self):
        text_field = self.find_element(
            TestSearchLocators.LOCATOR_TEXT_FIELD, time=3)
        text = text_field.text
        logging.info(
            f"We find text {text} in text field {TestSearchLocators.LOCATOR_TEXT_FIELD[1]}")
        return text
