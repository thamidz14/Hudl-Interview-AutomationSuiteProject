import pytest
import time
import random
import string
import allure
from pages.login_page import LoginPage
from pages.pswrd_page import PasswordPage
from pages.reset_pswrd_page import ResetPasswordPage
from pages.create_account_page import CreateAccountPage
from utils.testdata import random_email, random_first_name, random_last_name, random_password

LOGIN_URL = "https://identity.hudl.com/u/login/identifier?state=hKFo2SAyNEk1dTU0UkkwclVFcDJVVFI3N2hJUmlVcHFiMTBfVKFur3VuaXZlcnNhbC1sb2dpbqN0aWTZIENjRXpENWJHUWVBekg0TjRjUFRQWUV3WG9nSERBTnE3o2NpZNkgbjEzUmZrSHpLb3phTnhXQzVkWlFvYmVXR2Y0V2pTbjU"
CREATE_ACCOUNT_URL = "https://www.hudl.com/register"

# Utility for random password

def generate_weak_password():
    # Only lowercase, less than 8 chars
    return ''.join(random.choices(string.ascii_lowercase, k=6))

@allure.title("Login with Invalid Username")
@allure.description("Verify that login fails and shows an error when an invalid username (not an email) is used.")

@pytest.mark.parametrize("invalid_username", [
    ".", "invalid@", "user@", "@domain.com", "noatsymbol.com", "", "user@domain", "user@domain,com", "   ", "   @.com", "   a$%6@.com",
])
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

@pytest.mark.parametrize("invalid_password", [
    "wrongpassword123", "      ", "12345678", "password", "qwerty", "test1234", " ", "abcABC123", "!@#$%^&*"
])
def test_login_valid_username_invalid_password(browser, invalid_password):
    browser.get(LOGIN_URL)
    login_page = LoginPage(browser)
    login_page.enter_username("thamidzaman96@gmail.com")
    login_page.click_continue_username()
    password_page = PasswordPage(browser)
    password_page.enter_password(invalid_password)
    password_page.click_continue_password()
    time.sleep(2)
    # Should show error or stay on password page
    assert "password" in browser.current_url and "incorrect" in browser.page_source.lower() and "error" in browser.page_source.lower()


def test_reset_password_with_invalid_email_reset_page(browser):
    browser.get(LOGIN_URL)
    login_page = LoginPage(browser)
    login_page.enter_username("validuser@example.com")
    login_page.click_continue_username()
    password_page = PasswordPage(browser)
    password_page.click_forgot_password_button()
    reset_page = ResetPasswordPage(browser)
    reset_page.clear_email_field()
    reset_page.enter_email("notanemail")
    reset_page.click_continue()
    time.sleep(2)
    # Should show error or not proceed
    assert "reset" in browser.current_url or "Enter a valid email" in browser.page_source or "error" in browser.page_source.lower()

def test_create_account_with_existing_email(browser):
    browser.get(LOGIN_URL)
    login_page = LoginPage(browser)
    login_page.click_create_account_button()
    create_account_page = CreateAccountPage(browser)
    create_account_page.enter_first_name("John")
    create_account_page.enter_last_name("Doe")
    create_account_page.enter_email("thamidzaman96@gmail.com")  # Assume this exists
    create_account_page.click_create_account()
    time.sleep(2)
    password = random_password(12)
    create_account_page.enter_password(password)
    create_account_page.click_continue_account()
    time.sleep(2)
    # Should show error or not proceed
    assert "error" in browser.page_source.lower() or "already" in browser.page_source.lower() or "exists" in browser.page_source.lower()

@pytest.mark.parametrize("weak_password", [
    "abcdef",           # too short, only lowercase
    "1234567",          # only digits
    "password",         # common weak password
    "abc123",           # short, letters and digits
    "abcdefgh",         # just letters, long enough but weak
    "ABCDEFGH",         # just uppercase
    "abcABC",           # mixed case, too short
])
def test_create_account_with_weak_password(browser, weak_password):
    browser.get(LOGIN_URL)
    login_page = LoginPage(browser)
    login_page.click_create_account_button()
    create_account_page = CreateAccountPage(browser)
    create_account_page.enter_first_name("Jane")
    create_account_page.enter_last_name("Smith")
    email = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)) + '@gmail.com'
    create_account_page.enter_email(email)
    create_account_page.click_create_account()
    time.sleep(2)
    create_account_page.enter_password(weak_password)
    create_account_page.click_continue_account()
    time.sleep(2)
    # Should show error or not proceed
    assert "weak" in browser.page_source.lower() or "error" in browser.page_source.lower() or "password" in browser.page_source.lower()

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
