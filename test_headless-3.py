from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pytest
import os
import random

@pytest.fixture(params=["chrome-Windows11", "firefox-macOSVentura"],scope="class")
def driver(request):
    username = os.getenv("LT_USERNAME")
    accessToken = os.getenv("LT_ACCESS_KEY")
    gridUrl = "hub.lambdatest.com/wd/hub"

    if request.param == "chrome-Windows11":
        web_driver = webdriver.ChromeOptions()
        platform = "Windows 11"
    if request.param == "firefox-macOSVentura":
        web_driver = webdriver.FirefoxOptions()
        platform = "MacOS Ventura"

    lt_options = {
        "user": username,
        "accessKey": accessToken,
        "build": "your build",
        "name": "your test",
        "platformName": platform,
        "w3c": True,
        "browserName": "Chrome",
        "browserVersion": "latest",
        "selenium_version": "4.8.0",
        "headless": True
    }
    options = web_driver
    options.set_capability('LT:Options', lt_options)

    url = "https://"+username+":"+accessToken+"@"+gridUrl
    
    driver = webdriver.Remote(
        command_executor=url,
        options=options
    )

    yield driver
    
    driver.quit

def test_register_account_form(driver):
    driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/register")

    first_name = driver.find_element(By.ID, "input-firstname")
    first_name.send_keys("FirstName")

    last_name = driver.find_element(By.ID, "input-lastname")
    last_name.send_keys("LastName")

    random_number = str(random.randrange(1, 5000, 1))

    email = driver.find_element(By.ID, "input-email")
    email.send_keys("blogtest+" + random_number +"@example.com")

    telephone = driver.find_element(By.ID, "input-telephone")
    telephone.send_keys("+351999888777")

    password = driver.find_element(By.ID, "input-password")
    password.send_keys("123456")

    password_confirm = driver.find_element(By.ID, "input-confirm")
    password_confirm.send_keys("123456")

    newsletter = driver.find_element(By.XPATH, value="//label[@for='input-newsletter-yes']")
    newsletter.click()

    terms = driver.find_element(By.XPATH, value="//label[@for='input-agree']")
    terms.click()

    continue_button = driver.find_element(By.XPATH, value="//input[@value='Continue']")
    continue_button.click()

    assert driver.title == "Your Account Has Been Created!"