"""
UI tests using Playwright against https://www.saucedemo.com
— a publicly available demo e-commerce site built for QA practice.
"""
import pytest
from playwright.sync_api import Page, expect


BASE_URL = "https://www.saucedemo.com"


class TestLogin:

    def test_valid_login_redirects_to_inventory(self, page: Page):
        page.goto(BASE_URL)
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")
        expect(page).to_have_url(f"{BASE_URL}/inventory.html")

    def test_invalid_login_shows_error(self, page: Page):
        page.goto(BASE_URL)
        page.fill("#user-name", "wrong_user")
        page.fill("#password", "wrong_pass")
        page.click("#login-button")
        expect(page.locator(".error-message-container")).to_be_visible()

    def test_empty_username_shows_error(self, page: Page):
        page.goto(BASE_URL)
        page.fill("#password", "secret_sauce")
        page.click("#login-button")
        expect(page.locator(".error-message-container")).to_be_visible()

    def test_page_title_is_swag_labs(self, page: Page):
        page.goto(BASE_URL)
        expect(page).to_have_title("Swag Labs")


class TestInventory:

    def test_inventory_shows_6_products(self, page: Page):
        page.goto(BASE_URL)
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")
        items = page.locator(".inventory_item")
        expect(items).to_have_count(6)

    def test_add_to_cart_updates_badge(self, page: Page):
        page.goto(BASE_URL)
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")
        page.locator(".btn_primary.btn_inventory").first.click()
        expect(page.locator(".shopping_cart_badge")).to_have_text("1")

    def test_product_names_are_visible(self, page: Page):
        page.goto(BASE_URL)
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")
        first_item = page.locator(".inventory_item_name").first
        expect(first_item).to_be_visible()


class TestLogout:

    def test_logout_redirects_to_login(self, page: Page):
        page.goto(BASE_URL)
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")
        page.click("#react-burger-menu-btn")
        page.click("#logout_sidebar_link")
        expect(page).to_have_url(BASE_URL + "/")