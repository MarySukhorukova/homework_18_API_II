import os

from allure_commons._allure import step
from dotenv import load_dotenv
from selene import have, be
from selene.support.shared import browser


load_dotenv()
login = os.getenv("LOGIN")


def test_login(auth_via_api):

    auth_via_api.open("")

    with step("Verify successful authorization"):
        auth_via_api.element(".account").should(have.text(login))


def test_open_product_card(auth_via_api):

    auth_via_api.open("/smartphone")

    with step("Verify cart product open"):
        auth_via_api.element('input.product-box-add-to-cart-button').click()
        auth_via_api.element('div.product-name').should(be.visible)


def test_successful_search(auth_via_api):

    auth_via_api.open("")
    auth_via_api.element('[value="Search store"]').type('14.1-inch Laptop').press_enter()

    with step("Verify product found"):
        auth_via_api.element('.product-title').should(have.text('14.1-inch Laptop'))


def test_unsuccessful_search(auth_via_api):

    auth_via_api.open("")
    auth_via_api.element('[value="Search store"]').type('Lapptop').press_enter()

    with step("Verify product found"):
        auth_via_api.element('.search-results').should(have.text('No products were found that matched your criteria.'))


def test_add_product_to_cart(auth_via_api):

    auth_via_api.open("/computing-and-internet")
    auth_via_api.element('input#add-to-cart-button-13').click()
    auth_via_api.element('li#topcartlink > a').click()
    auth_via_api.driver.refresh()

    auth_via_api.element('td.product > a').should(have.text('Computing and Internet'))

    auth_via_api.element('td.remove-from-cart > input').click()
    auth_via_api.element('input.update-cart-button').click()
    auth_via_api.element('.order-summary-content').should(have.text('Your Shopping Cart is empty!'))