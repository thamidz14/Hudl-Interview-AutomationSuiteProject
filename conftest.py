import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

'''
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Attach screenshot to Allure on failure
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("browser")
        if driver:
            try:
                allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
            except Exception as e:
                pass
'''

@pytest.fixture
def browser():
    options = Options()
    #options.add_argument("--headless=False")  # Run in headless mode
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)  # Wait up to 10 seconds for elements
    driver.maximize_window()
    yield driver
    driver.quit()
