
class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.cart_badge = page.locator(".shopping_cart_badge")

    def add_product_to_cart(self,product_name):
        self.page.locator(".inventory_item").filter(has_text=product_name).get_by_role("button",name="Add to cart").click()

    def get_cart_count(self):
        return self.cart_badge.text_content()

    def sortorder(self):
        self.page.locator(".product_sort_container").select_option(label="Name (Z to A)")
        self.page.wait_for_timeout(3000)

    def autoscroll(self):
        self.page.locator(".footer_copy").scroll_into_view_if_needed()
        self.page.wait_for_timeout(9000)