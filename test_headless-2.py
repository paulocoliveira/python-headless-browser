from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def test_register_account_form():
    # Create an instance of ChromeOptions
    chrome_options = Options()

    # Configure ChromeOptions to run in headless mode
    chrome_options.add_argument('--headless')

    # Initialize the WebDriver with the configured ChromeOptions
    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/register")

    first_name = driver.find_element(By.ID, "input-firstname")
    first_name.send_keys("FirstName")

    last_name = driver.find_element(By.ID, "input-lastname")
    last_name.send_keys("LastName")

    email = driver.find_element(By.ID, "input-email")
    email.send_keys("blogtest+223@example.com")

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