from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        """
        Конструктор класса BasePage.
        Args:
            driver: Объект WebDriver для взаимодействия с браузером.
        """
        self.driver = driver
        self.base_url = "https://testpages.eviltester.com/styled/apps/triangle/triangle001.html"

    def find_element(self, locator, time=10):
        """
        Метод для поиска элемента на странице.
        Args:
            locator: Локатор элемента (например, (By.ID, 'element_id'))
            time: Время ожидания (по умолчанию 10 секунд).
        Returns:
            Найденный элемент.
        Raises:
            TimeoutException: Если элемент не найден в течение указанного времени.
        """
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}")

    def get_element_property(self, locator, property):
        """
        Метод для получения значения CSS-свойства элемента.
        Args:
            locator: Локатор элемента.
            property: Имя CSS-свойства (например, 'color').
        Returns:
            Значение указанного CSS-свойства элемента.
        """
        element = self.find_element(locator)
        return element.value_of_css_property(property)

    def go_to_site(self):
        """
        Метод для перехода на базовый URL веб-приложения.
        """
        return self.driver.get(self.base_url)


help(BasePage)
