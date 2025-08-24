import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_login_regression(browser):
    browser.get("http://example.com/login")
    browser.find_element(By.ID, "username").send_keys("test_user")
    browser.find_element(By.ID, "password").send_keys("1234")
    browser.find_element(By.ID, "login-btn").click()
    
    assert "Dashboard" in browser.page_source
