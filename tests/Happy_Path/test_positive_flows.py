import pytest
import time
import json
import allure
from pages.login_page import LoginPage
from pages.pswrd_page import PasswordPage
from pages.reset_pswrd_page import ResetPasswordPage
from pages.create_account_page import CreateAccountPage 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By 
from utils.testdata import random_email, random_password
from dotenv import load_dotenv
import os

from utils.config import LOGIN_URL, PASSWORD_URL


load_dotenv()

# 1. Valid Login Flow
@allure.title("Valid Login Flow")
@allure.description("Verify that a user can successfully log in with valid credentials and is redirected to the dashboard.")
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
    # Wait until dashboard is loaded by checking for expected text
    WebDriverWait(browser, 10).until(lambda d: "Newcastle Jets FC" in d.page_source)
    # Assert login success (dashboard loaded)
    assert "Newcastle Jets FC" in browser.page_source

# 2. Reset Password Flow
@allure.title("Reset Password Flow")
@allure.description("Verify that the reset password flow works for a valid email, and the user is prompted to check their email.")
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
@allure.title("Go Back from Reset Password")
@allure.description("Verify that the user can navigate back to the login page from the reset password page.")
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
@allure.title("Access Create Account from Login Page")
@allure.description("Verify that the user can access the create account page directly from the login page.")
def test_access_create_account_from_login(browser):
    browser.get(LOGIN_URL)
    login_page = LoginPage(browser)
    login_page.click_create_account_button()
    time.sleep(2)
    # Assert navigation to create account page
    assert "signup" in browser.current_url or "Create Account" in browser.page_source

# 5. Create an Account from create account Access page
with open("utils/create_account_from_login_testdata.json") as f:
    create_account_from_login_testdata = json.load(f)
@pytest.mark.parametrize(
    "first_name,last_name",
    [(d["first_name"], d["last_name"]) for d in create_account_from_login_testdata]
)
@allure.title("Create Account from Create Account Access Page")
@allure.description("Verify that a user can start the account creation flow from the main create account page using various valid data sets.")
def test_create_account_from_login(browser, first_name, last_name):
    browser.get(LOGIN_URL)
    login_page = LoginPage(browser)
    login_page.click_create_account_button()
    create_account_page = CreateAccountPage(browser)
    # Randomize email to avoid collisions
    create_account_page.enter_first_name(first_name)
    create_account_page.enter_last_name(last_name)
    create_account_page.enter_email(random_email())
    create_account_page.click_create_account()
    time.sleep(2)
    create_account_page.enter_password(random_password(12))
    create_account_page.click_continue_account()
    time.sleep(2)
    # Assert navigation to create account page
    assert "fan" in browser.current_url or "Find livestreams" in browser.page_source
    
# 6. Access Create Account Page from Password Page
@allure.title("Access Create Account from Password Page")
@allure.description("Verify that the user can access the create account page from the password entry page.")
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


# 7. Access Create Account Page and Create an Account from Password Page
with open("utils/create_account_testdata.json") as f:
    create_account_testdata = json.load(f)
@pytest.mark.parametrize(
    "first_name,last_name",
    [(d["first_name"], d["last_name"]) for d in create_account_testdata]
)
@allure.title("Create Account from Password Page with Data-Driven Inputs")
@allure.description("Verify that a user can access the create account page from the password page and successfully create an account using random email and password.")
def test_access_create_account_page_and_create_account_from_password_page(browser, first_name, last_name):
    browser.get(LOGIN_URL)
    login_page = LoginPage(browser)
    login_page.enter_username(random_email())
    login_page.click_continue_username()
    time.sleep(2)
    password_page = PasswordPage(browser)
    password_page.click_create_account_button()
    time.sleep(2)
    create_account_page = CreateAccountPage(browser)
    create_account_page.enter_first_name(first_name)
    create_account_page.enter_last_name(last_name)
    create_account_page.click_create_account()
    time.sleep(2)
    create_account_page.enter_password(random_password(12))
    create_account_page.click_continue_account()
    time.sleep(4)
    # Assert navigation to create account page
    assert "fan" in browser.current_url or "Find livestreams" in browser.page_source
