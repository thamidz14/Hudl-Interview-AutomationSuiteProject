import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def browser():
    options = Options()
    #options.add_argument("--headless=False")  # Run in headless mode
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)  # Wait up to 10 seconds for elements
    yield driver
    driver.quit()
