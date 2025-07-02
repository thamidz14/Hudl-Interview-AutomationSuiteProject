from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, "username")
        self.create_account_button = (By.XPATH, "//a[@class='c15c36395 c0e6110c2']")
        self.continue_username_button = (By.XPATH, "//button[@class='ccbf5f810 c0a334fa0 c8f34b77b cec7560fc _button-login-id']")
        self.login_button = (By.ID, "login-button")
        
    def open(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        self.driver.find_element(*self.username_field).send_keys(username)
    
    def click_continue_username(self):
        self.driver.find_element(*self.continue_username_button).click()

    def click_create_account_button(self):
        self.driver.find_element(*self.create_account_button).click()
    