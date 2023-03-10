import os

from allure_commons._allure import step
from dotenv import load_dotenv
from selene import have, be
from selene.support.shared import browser


load_dotenv()
login = os.getenv("LOGIN")


def test_login(auth_via_api):

    browser.open("")

    with step("Verify successful authorization"):
        browser.element(".account").should(have.text(login))


def test_open_product_card(auth_via_api):

    browser.open("/smartphone")

    with step("Verify cart product open"):
        browser.element('input.product-box-add-to-cart-button').click()
        browser.element('div.product-name').should(be.visible)


def test_successful_search(auth_via_api):

    browser.open("")
    browser.element('[value="Search store"]').type('14.1-inch Laptop').press_enter()

    with step("Verify product found"):
        browser.element('.product-title').should(have.text('14.1-inch Laptop'))


def test_unsuccessful_search(auth_via_api):

    browser.open("")
    browser.element('[value="Search store"]').type('Lapptop').press_enter()

    with step("Verify product found"):
        browser.element('.search-results').should(have.text('No products were found that matched your criteria.'))


def test_add_product_to_cart(auth_via_api):

    browser.open("/computing-and-internet")
    browser.element('input#add-to-cart-button-13').click()
    browser.element('li#topcartlink > a').click()
    browser.driver.refresh()

    browser.element('td.product > a').should(have.text('Computing and Internet'))

    browser.element('td.remove-from-cart > input').click()
    browser.element('input.update-cart-button').click()
    browser.element('.order-summary-content').should(have.text('Your Shopping Cart is empty!'))