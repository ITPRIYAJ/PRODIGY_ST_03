import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_positive_login(driver):
    driver.get("https://demowebshop.tricentis.com/")

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Log in']"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='Email']"))).send_keys("srinila@gmail.com")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='Password']"))).send_keys("Nila@123")

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='RememberMe']"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='button-1 login-button' or @value='Log in']"))).click()

    logout = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[text()='Log out']")))
    assert logout.is_displayed()

def test_invalid_username_login(driver):
    driver.get("https://demowebshop.tricentis.com/")

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Log in']"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='Email']"))).send_keys("invalid_username")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='Password']"))).send_keys("Nila@123")

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='RememberMe']"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='button-1 login-button' or @value='Log in']"))).click()

    error = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'message-error')]")))
    assert error.is_displayed()

def test_invalid_password_login(driver):
    driver.get("https://demowebshop.tricentis.com/")

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Log in']"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='Email']"))).send_keys("srinila@gmail.com")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='Password']"))).send_keys("invalid_password")

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='RememberMe']"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='button-1 login-button' or @value='Log in']"))).click()

    error = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'message-error')]")))
    assert error.is_displayed()

def test_empty_fields_login(driver):
    driver.get("https://demowebshop.tricentis.com/")

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Log in']"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='Email']"))).send_keys("")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='Password']"))).send_keys("")

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='RememberMe']"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='button-1 login-button' or @value='Log in']"))).click()

    error = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'message-error')]")))
    assert error.is_displayed()
