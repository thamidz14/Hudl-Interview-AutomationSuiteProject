import pytest
from selenium import webdriver
from pages.login_page import LoginPage

def test_valid_login(browser):
    login_page = LoginPage(browser)
    login_page.open("https://www.hudl.com/")
    login_page.enter_username("testuser")
    login_page.click_continue_username()
    login_page.enter_password("testpassword")
    login_page.click_continue_password()
    assert "Dashboard" in browser.title
    