import pytest 
from selenium import webdriver
from pages.login_page import Login

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get('https://www.saucedemo.com/v1/')
    yield driver
    driver.quit()

def test_valid_login():
    login_page = Login(driver)
    login_page.login("standard_user","secret_sauce")
    