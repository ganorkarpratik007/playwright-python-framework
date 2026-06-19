from playwright.sync_api import expect


def test_hover(page):
    page.goto("https://the-internet.herokuapp.com/hovers")
    page.locator(".figure").first.hover()
    textContent  = page.locator(".figcaption").first.text_content()
    assert "user1" in textContent
    print(textContent)

def test_checkbox(page):
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    expect(page.locator("input[type='checkbox']").first).not_to_be_checked()
    page.locator("input[type='checkbox']").first.check()
    expect(page.locator("input[type='checkbox']").first).to_be_checked()

def test_switchwindow(page):
    page.goto("https://the-internet.herokuapp.com/windows")
    with page.expect_popup() as popup:
         page.get_by_text("Click Here").click()
    new_page =popup.value
    expect(new_page.locator("h3")).to_have_text("New Window")

def test_iframe(page):
    page.goto("https://letcode.in/frame")
    page.frame_locator("#firstFr").get_by_placeholder("Enter name").fill("Sharukh")
    page.wait_for_timeout(5000)