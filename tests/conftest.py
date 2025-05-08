import os

import pytest
from dotenv import load_dotenv
from selene.support.shared import browser
from utils.base_session import BaseSession


load_dotenv()

@pytest.fixture(scope="session")
def demoshop():
    web_url = os.getenv("WEB_URL")
    return BaseSession(web_url)


@pytest.fixture(scope="session")
def reqres():
    api_url = os.getenv("API_URL")
    return BaseSession(api_url)


@pytest.fixture(scope='session')
def auth_via_api(demoshop):
    browser.config.base_url = os.getenv("WEB_URL")
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    response = demoshop.post("/login", json={"Email": os.getenv("LOGIN"), "Password": os.getenv("PASSWORD")},
                             allow_redirects=False)
    authorization_cookie = response.cookies.get("NOPCOMMERCE.AUTH")
    browser.open("/Themes/DefaultClean/Content/images/logo.png")
    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": authorization_cookie})
    return browser
    