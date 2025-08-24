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


def test_homepage_stress():
    for _ in range(50):  # simulate 50 refresh
        driver = webdriver.Chrome()
        driver.get("http://example.com/")
        assert "Welcome" in driver.page_source
        driver.quit()
        

def test_sanity():
    driver = webdriver.Chrome()
    driver.get("http://example.com")
    assert "Example" in driver.title
    driver.quit()
    
    
def test_sql_injection():
    driver = webdriver.Chrome()
    driver.get("http://example.com/login")
    driver.find_element(By.ID, "username").send_keys("' OR '1'='1")
    driver.find_element(By.ID, "password").send_keys("dummy")
    driver.find_element(By.ID, "login-btn").click()

    # ถ้า login สำเร็จแสดงว่าไม่ปลอดภัย
    assert "Dashboard" not in driver.page_source
    driver.quit()