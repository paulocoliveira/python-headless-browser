from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def test_simple_demo_form():
    # Create an instance of ChromeOptions
    chrome_options = Options()

    # Configure ChromeOptions to run in headless mode
    chrome_options.add_argument('--headless')

    # Initialize the WebDriver with the configured ChromeOptions
    driver = webdriver.Chrome(options=chrome_options)

    # Load a webpage
    driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")

    # Find an input element by its ID and enter text
    input_element = driver.find_element(By.ID, "user-message")
    input_element.send_keys("This is a headless browser text!")

    # Find an element by its ID and click on it
    element = driver.find_element(By.ID, "showInput")
    element.click()

    # Find an element by its ID and extract its text
    element = driver.find_element(By.ID, "message")
    print(element.text)