from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_add_to_cart(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user","secret_sauce")

    inventory_page = InventoryPage(page)
    inventory_page.add_product_to_cart("Sauce Labs Backpack")

    assert inventory_page.get_cart_count() == "1"

    inventory_page.sortorder()

    inventory_page.autoscroll()



