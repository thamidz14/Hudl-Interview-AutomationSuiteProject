import pytest
import time
import random
import string
from pages.login_page import LoginPage
from pages.pswrd_page import PasswordPage
from pages.reset_pswrd_page import ResetPasswordPage
from pages.create_account_page import CreateAccountPage 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By 
from utils.testdata import random_email, random_first_name, random_last_name, random_password
from dotenv import load_dotenv
import os

LOGIN_URL = "https://identity.hudl.com/u/login/identifier?state=hKFo2SAyNEk1dTU0UkkwclVFcDJVVFI3N2hJUmlVcHFiMTBfVKFur3VuaXZlcnNhbC1sb2dpbqN0aWTZIENjRXpENWJHUWVBekg0TjRjUFRQWUV3WG9nSERBTnE3o2NpZNkgbjEzUmZrSHpLb3phTnhXQzVkWlFvYmVXR2Y0V2pTbjU"
PASSWORD_URL = "https://identity.hudl.com/u/login/password?state=hKFo2SAyNEk1dTU0UkkwclVFcDJVVFI3N2hJUmlVcHFiMTBfVKFur3VuaXZlcnNhbC1sb2dpbqN0aWTZIENjRXpENWJHUWVBekg0TjRjUFRQWUV3WG9nSERBTnE3o2NpZNkgbjEzUmZrSHpLb3phTnhXQzVkWlFvYmVXR2Y0V2pTbjU"

RESET_PASSWORD_URL = "https://identity.hudl.com/u/reset-password/request/prod-hudl-users-terraform?state=hKFo2SAwVWdRZVlNY2NKSVZ5SGNwbU83Ym9zZGItUU1DNXVFaqFurnJlc2V0LXBhc3N3b3Jko3RpZNkgLTh2TngzckThZVpkdmJkOGNGQWRlM3hIX3Frd0c5aWKjY2lk2SBuMTNSZmtIektvemFOeFdDNWRaUW9iZVdHZjRXalNuNQ"  # Adjust if needed
CREATE_ACCOUNT_URL = "https://www.hudl.com/register"  # Adjust if needed

load_dotenv()

# 1. Valid Login Flow

def test_valid_login_flow(browser):
    browser.get(LOGIN_URL) 
    login_page = LoginPage(browser)
    login_page.enter_username("thamidzaman96@gmail.com")
    login_page.click_continue_username()
    password_page = PasswordPage(browser)
    # Load password securely from environment variable
    password = os.environ.get("HUDL_TEST_PASSWORD")
    password_page.enter_password(password)
    password_page.click_continue_password()
    time.sleep(5)
    # Assert login success (dashboard loaded)
    assert "Newcastle Jets FC" in browser.page_source
'''
# 2. Reset Password Flow
def test_reset_password_flow(browser):
    browser.get(LOGIN_URL) 
    login_page = LoginPage(browser)
    login_page.enter_username(random_email())
    login_page.click_continue_username()
    password_page = PasswordPage(browser)
    password_page.click_forgot_password_button()
    reset_page = ResetPasswordPage(browser)
    reset_page.click_continue()
    # Assert confirmation (adjust selector/message as needed)
    assert "Check your email" in browser.page_source or "reset" in browser.current_url

# 3. Go Back from Reset Password
def test_go_back_from_reset_password(browser):
    browser.get(LOGIN_URL) 
    login_page = LoginPage(browser)
    login_page.enter_username(random_email())
    login_page.click_continue_username()
    password_page = PasswordPage(browser)
    password_page.click_forgot_password_button()
    reset_page = ResetPasswordPage(browser)
    reset_page.click_go_back()
    time.sleep(2)
    # Assert returned to login page
    assert "login" in browser.current_url or "Log In" in browser.page_source

# 4. Access Create Account Page from Login Page
def test_access_create_account_from_login(browser):
    browser.get(LOGIN_URL)
    login_page = LoginPage(browser)
    login_page.click_create_account_button()
    # Assert navigation to create account page
    assert "signup" in browser.current_url or "Create Account" in browser.page_source

# 5. Create an Account from create account Access page
def test_create_account_from_login(browser):
    browser.get(LOGIN_URL)
    login_page = LoginPage(browser)
    login_page.click_create_account_button()
    create_account_page = CreateAccountPage(browser)
    first_name = random_first_name()
    last_name = random_last_name()
    email = random_email()
    password = random_password(12)
    create_account_page.enter_first_name(first_name)
    create_account_page.enter_last_name(last_name)
    create_account_page.enter_email(email)
    create_account_page.click_create_account()
    time.sleep(2)
    create_account_page.enter_password(password)
    create_account_page.click_continue_account()
    time.sleep(2)
    # Assert navigation to create account page
    assert "fan" in browser.current_url or "Find livestreams" in browser.page_source
    
# 6. Access Create Account Page from Password Page
def test_access_create_account_page_from_password_page(browser):
    browser.get(LOGIN_URL)
    login_page = LoginPage(browser)
    login_page.enter_username("validuser@example.com")
    login_page.click_continue_username()
    password_page = PasswordPage(browser)
    time.sleep(2)
    password_page.click_create_account_button()
    time.sleep(2)
    assert "signup" in browser.current_url or "Create Account" in browser.page_source
'''

# 7. Access Create Account Page and Create an Account from Password Page
import pytest

@pytest.mark.parametrize(
    "first_name,last_name,email,password",
    [
        (random_first_name(), random_last_name(), random_email(), random_password(12)),
        (random_first_name(), random_last_name(), random_email(), random_password(12)),
        (random_first_name(), random_last_name(), random_email(), random_password(12)),
    ]
)
def test_access_create_account_page_and_create_account_from_password_page(browser, first_name, last_name, email, password):
    browser.get(LOGIN_URL)
    login_page = LoginPage(browser)
    login_page.enter_username(email)
    login_page.click_continue_username()
    password_page = PasswordPage(browser)
    time.sleep(2)
    password_page.click_create_account_button()
    time.sleep(2)
    create_account_page = CreateAccountPage(browser)
    create_account_page.enter_first_name(first_name)
    create_account_page.enter_last_name(last_name)
    create_account_page.click_create_account()
    time.sleep(2)
    create_account_page.enter_password(password)
    create_account_page.click_continue_account()
    time.sleep(4)
    # Assert navigation to create account page
    assert "fan" in browser.current_url or "Find livestreams" in browser.page_source
