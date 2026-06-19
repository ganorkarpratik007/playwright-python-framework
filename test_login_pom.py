import pytest
from playwright.sync_api import sync_playwright, expect

from pages.login_page import LoginPage

@pytest.mark.parametrize("username,password", [
    ("Admin","admin123"),
    ("Admin","wrongpass"),
    ("InvalidUser","admin123")
])

def test_login_pom(page,username,password):
            login_page = LoginPage(page)
            login_page.goto()
            login_page.login(username,password)

            expect(page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")

