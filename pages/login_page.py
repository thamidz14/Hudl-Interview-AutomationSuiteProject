from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, "username")
        self.password_field = (By.ID, "password")
        self.continue_username_button = (By.CLASS_NAME, "ccbf5f810 c0a334fa0 c8f34b77b cec7560fc_button-login-id")
        self.continue_password_button = (By.CLASS_NAME, "ccbf5f810 c0a334fa0 c8f34b77b cec7560fc_button-login-password")
        self.login_button = (By.ID, "login-button")
        
    def open(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        self.driver.find_element(*self.username_field).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)
    
    def click_continue_username(self):
        self.driver.find_element(*self.continue_username_button).click()
    
    def click_continue_password(self):
        self.driver.find_element(*self.continue_password_button).click()
    
    
        
    