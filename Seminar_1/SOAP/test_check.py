from check_text import check_text
import pytest


def test_step1():
    assert "молоко" in check_text("малако")


if __name__ == '__main__':
    pytest.main(["-vv"])
