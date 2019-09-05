from pages.product_page import ProductPage
import time
import pytest

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
def test_guest_can_add_product_to_basket(browser,link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_btn()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_item_be_in_basket()
    time.sleep(10)

