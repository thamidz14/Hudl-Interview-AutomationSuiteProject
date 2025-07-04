import pytest
import time
import allure
import json
from pages.login_page import LoginPage
from pages.pswrd_page import PasswordPage
from pages.reset_pswrd_page import ResetPasswordPage
from pages.create_account_page import CreateAccountPage
from utils.testdata import random_email, random_password
from utils.config import LOGIN_URL, PASSWORD_URL
import itertools

# Helper to load invalid usernames from file
with open("utils/invalid_usernames.json") as f:
    invalid_usernames = json.load(f)
@allure.title("Login with Invalid Username")
@allure.description("Verify that login fails and shows an error when an invalid username (not an email) is used.")
@pytest.mark.parametrize("invalid_username", invalid_usernames)
def test_login_with_invalid_username(browser, invalid_username):
    browser.get(LOGIN_URL)
    login_page = LoginPage(browser)
    if invalid_username == "":
        pytest.skip("Skipping empty username test. Cannot find element accessor for pop up message. Might be shadow DOM element")
    login_page.enter_username(invalid_username)
    login_page.click_continue_username()
    time.sleep(2)
    # Should stay on login or show error
    assert "login" in browser.current_url and "enter a valid email." in browser.page_source.lower() and "error" in browser.page_source.lower()


with open("utils/invalid_passwords.json") as f:
    invalid_passwords = json.load(f)
@allure.title("Login with Valid Username and Invalid Password")
@allure.description("Verify that login fails and shows an error when a valid username is used with an invalid password.")
@pytest.mark.parametrize("invalid_password", invalid_passwords)
def test_login_valid_username_invalid_password(browser, invalid_password):
    browser.get(LOGIN_URL)
    login_page = LoginPage(browser)
    login_page.enter_username("validuser@gmail.com")
    login_page.click_continue_username()
    password_page = PasswordPage(browser)
    password_page.enter_password(invalid_password)
    password_page.click_continue_password()
    time.sleep(2)
    # Should show error or stay on password page
    assert "password" in browser.current_url or "incorrect" in browser.page_source.lower() or "error" in browser.page_source.lower()


with open("utils/invalid_usernames.json") as f:
    invalid_usernames = json.load(f)
@allure.title("Reset Password with Invalid Email")
@allure.description("Verify that the reset password flow fails and shows an error when an invalid email is provided.")
@pytest.mark.parametrize("invalid_username", invalid_usernames)
def test_reset_password_with_invalid_username(browser, invalid_username):
    browser.get(LOGIN_URL)
    login_page = LoginPage(browser)
    login_page.enter_username("validuser@example.com")
    login_page.click_continue_username()
    password_page = PasswordPage(browser)
    password_page.click_forgot_password_button()
    reset_page = ResetPasswordPage(browser)
    reset_page.clear_email_field()
    reset_page.enter_email(invalid_username)
    reset_page.click_continue()
    time.sleep(2)
    # Should show error or not proceed
    assert "reset" in browser.current_url or "Enter a valid email" in browser.page_source or "error" in browser.page_source.lower()


with open("utils/existing_account_names.json") as f:
    existing_account_names = json.load(f)
first_names = existing_account_names["first_names"]
last_names = existing_account_names["last_names"]
@allure.title("Create Account with Existing Email")
@allure.description("Verify that creating an account with an already registered email fails, regardless of first or last name.")
@pytest.mark.parametrize("first_name,last_name", list(itertools.product(first_names, last_names)))
def test_create_account_with_existing_email(browser, first_name, last_name):
    browser.get(LOGIN_URL)
    login_page = LoginPage(browser)
    login_page.click_create_account_button()
    create_account_page = CreateAccountPage(browser)
    create_account_page.enter_first_name(first_name)
    create_account_page.enter_last_name(last_name)
    create_account_page.enter_email("thamidzaman96@gmail.com")  # Assume this exists
    create_account_page.click_create_account()
    time.sleep(2)
    password = random_password(12)
    create_account_page.enter_password(password)
    create_account_page.click_continue_account()
    time.sleep(2)
    # Should show error or not proceed
    assert "error" in browser.page_source.lower() or "already" in browser.page_source.lower() or "exists" in browser.page_source.lower()


with open("utils/weak_passwords.json") as f:
    weak_passwords = json.load(f)
@allure.title("Create Account with Weak Password")
@allure.description("Verify that account creation flow fails and shows an error when a weak password is used.")
@pytest.mark.parametrize("weak_password", weak_passwords)
def test_create_account_with_weak_password(browser, weak_password):
    browser.get(LOGIN_URL)
    login_page = LoginPage(browser)
    login_page.click_create_account_button()
    create_account_page = CreateAccountPage(browser)
    create_account_page.enter_first_name("Jane")
    create_account_page.enter_last_name("Smith")
    create_account_page.enter_email(random_email())
    create_account_page.click_create_account()
    time.sleep(2)
    create_account_page.enter_password(weak_password)
    create_account_page.click_continue_account()
    time.sleep(2)
    # Should show error or not proceed
    assert "weak" in browser.page_source.lower() or "error" in browser.page_source.lower() or "password" in browser.page_source.lower()

@allure.title("Create Account with Missing Fields")
@allure.description("Verify that account creation flow fails and shows an error when required fields are missing.")
def test_create_account_with_missing_fields(browser):
    browser.get(LOGIN_URL)
    login_page = LoginPage(browser)
    login_page.click_create_account_button()
    create_account_page = CreateAccountPage(browser)
    # Leave all fields blank and try to create account
    create_account_page.click_create_account()
    time.sleep(2)
    # Should show error or not proceed
    assert "required" in browser.page_source.lower() or "error" in browser.page_source.lower() or "missing" in browser.page_source.lower()
