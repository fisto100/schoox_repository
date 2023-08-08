import pytest
from selenium import webdriver


@pytest.fixture()
def setup(request):

    driver = webdriver.Chrome()
    driver.implicitly_wait(6)
    driver.get("http://qatest.schoox.com/login")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()
