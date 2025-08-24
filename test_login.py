# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import pytest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# ตั้งค่า logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@pytest.fixture
def browser():
    logging.info("เปิด Chrome Browser แบบ headless")
    options = Options()
    options.add_argument("--headless=new")  
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    yield driver
    logging.info("ปิด Browser")
    driver.quit()

def test_open_google(browser):
    logging.info("ไปที่เว็บ Google")
    browser.get("https://www.google.com")
    
    logging.info("ตรวจสอบ title ของหน้าเว็บ")
    assert "Google" in browser.title
    logging.info("เปิดเว็บ Google สำเร็จ")


# def test_login(browser):
#     browser.get("http://example.com/login")
#     WebDriverWait(browser, 10).until(
#         EC.presence_of_element_located((By.ID, "username"))
#     ).send_keys("test_user")
    
#     browser.find_element(By.ID, "password").send_keys("1234")
#     browser.find_element(By.ID, "login-btn").click()
    
#     WebDriverWait(browser, 10).until(
#         EC.presence_of_element_located((By.ID, "dashboard"))
#     )
#     assert "Dashboard" in browser.page_source



# def test_login(browser):
#     browser.get("http://example.com/login")
#     WebDriverWait(browser, 10).until(
#         EC.presence_of_element_located((By.ID, "username"))
#     ).send_keys("test_user")
    
#     browser.find_element(By.ID, "password").send_keys("1234")
#     browser.find_element(By.ID, "login-btn").click()
    
#     WebDriverWait(browser, 10).until(
#         EC.presence_of_element_located((By.ID, "dashboard"))
#     )
#     assert "Dashboard" in browser.page_source



# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# @pytest.fixture
# def browser():
#     options = Options()
#     options.add_argument("--headless")  # run headless
#     options.add_argument("--no-sandbox")
#     options.add_argument("--disable-dev-shm-usage")
#     options.add_argument("--disable-gpu")
#     options.add_argument("--remote-debugging-port=9222")

#     driver = webdriver.Chrome(options=options)
#     yield driver
#     driver.quit()

# def test_login_regression(browser):
#     browser.get("https://your-real-login-page.com/login")
#     username_input = WebDriverWait(browser, 10).until(
#         EC.presence_of_element_located((By.ID, "username"))
#     )
#     username_input.send_keys("test_user")
#     assert "Dashboard" in browser.page_source
    
    
# def test_login_regression2(browser):
#     browser.get("http://example.com/login")
#     browser.find_element(By.ID, "username").send_keys("test_user")
#     browser.find_element(By.ID, "password").send_keys("1234")
#     browser.find_element(By.ID, "login-btn").click()
    
#     assert "Dashboard" in browser.page_source
