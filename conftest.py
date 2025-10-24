import pytest
from selenium import webdriver
from utils import login

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver

@pytest.fixture
def login_in_driver(driver):
    login(driver)
    return driver    

