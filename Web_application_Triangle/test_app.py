from testpage import OperationsHelper
import logging
import yaml
import pytest

with open("testdata.yaml", encoding="utf-8") as f:
    testdata = yaml.safe_load(f)


def test_1(browser):
    """
    Проверяем треугольник на равнобедренность, 
    вводя валидные данные в приложение.
    """
    logging.info("Test Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_side1(testdata.get("test1")[0])
    testpage.enter_side2(testdata.get("test1")[1])
    testpage.enter_side3(testdata.get("test1")[2])
    testpage.click_button()
    assert "isosceles" in testpage.get_text().lower(), "test FAILED"


def test_2(browser):
    """
    Проверяем треугольник на равносторонность, 
    вводя валидные данные в приложение.
    """
    logging.info("Test Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_side1(testdata.get("test2")[0])
    testpage.enter_side2(testdata.get("test2")[1])
    testpage.enter_side3(testdata.get("test2")[2])
    testpage.click_button()
    assert "equilateral" in testpage.get_text().lower(), "test FAILED"


def test_3(browser):
    """
    Проверяем треугольник на разносторонность, 
    вводя валидные данные в приложение.
    """
    logging.info("Test Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_side1(testdata.get("test3")[0])
    testpage.enter_side2(testdata.get("test3")[1])
    testpage.enter_side3(testdata.get("test3")[2])
    testpage.click_button()
    assert "scalene" in testpage.get_text().lower(), "test FAILED"


@pytest.mark.parametrize("test_name, side_values", [
    ("test4", [0, 0, 0]),
    ("test5", [-2, 3, 4]),
    ("test6", [10, 20, 10])
])
def test_4_5_6(browser, test_name, side_values):
    """
    Вводим невалидные данные в приложение,
    объединив три однотипных теста с помощью фикстуры @pytest.mark.parametrize.
    """
    logging.info("Test Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    side1, side2, side3 = side_values
    testpage.enter_side1(side1)
    testpage.enter_side2(side2)
    testpage.enter_side3(side3)
    testpage.click_button()
    assert "error: not a triangle" in testpage.get_text(
    ).lower(), f"{test_name} FAILED"


@pytest.mark.parametrize("test_name, side_values", [
    ("test4", ["aба", 20, 10]),
    ("test5", [10, "aба", 10]),
    ("test6", [10, 20, "aба"])
])
def test_7_8_9(browser, test_name, side_values):
    """
    Вводим невалидные данные в приложение,
    объединив три однотипных теста с помощью фикстуры @pytest.mark.parametrize.
    """
    logging.info("Test Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    side1, side2, side3 = side_values
    testpage.enter_side1(side1)
    testpage.enter_side2(side2)
    testpage.enter_side3(side3)
    testpage.click_button()
    assert "error: side 1 is not a number" or "error: side 2 is not a number" or "error: side 3 is not a number" in testpage.get_text(
    ).lower(), f"{test_name} FAILED"


def test_10(browser):
    """
    Ввод большого валидного числа.
    """
    logging.info("Test Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_side1(testdata.get("test10")[0])
    testpage.enter_side2(testdata.get("test10")[1])
    testpage.enter_side3(testdata.get("test10")[2])
    testpage.click_button()
    assert "isosceles" in testpage.get_text().lower(), "test FAILED"


def test_12(browser):
    """
    Ввод пустых полей.
    """
    logging.info("Test Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_side1(testdata.get("test12")[0])
    testpage.enter_side2(testdata.get("test12")[1])
    testpage.enter_side3(testdata.get("test12")[2])
    testpage.click_button()
    assert "error: side 1 is missing" in testpage.get_text().lower(), "test FAILED"


def test_12(browser):
    """
    Проверка на XSS уязвимость
    """
    logging.info("Test Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_side1(testdata.get("test12")[0])
    testpage.enter_side2(testdata.get("test12")[1])
    testpage.enter_side3(testdata.get("test12")[2])
    testpage.click_button()
    assert "error: side 1 is not a number" in testpage.get_text().lower(), "test FAILED"
