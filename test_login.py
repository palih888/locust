import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def browser():
    options = Options()
    options.add_argument("--headless")  # run headless
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--remote-debugging-port=9222")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_login_regression(browser):
    browser.get("http://example.com/login")
    browser.find_element(By.ID, "username").send_keys("test_user")
    browser.find_element(By.ID, "password").send_keys("1234")
    browser.find_element(By.ID, "login-btn").click()
    
    assert "Dashboard" in browser.page_source
