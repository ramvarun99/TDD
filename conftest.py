import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = None


@pytest.fixture()
def setup(request):
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()
