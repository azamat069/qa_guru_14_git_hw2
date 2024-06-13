import pytest
from selene import browser, be, have

@pytest.fixture(scope='function', autouse=True)
def browser_management():
    yield
    browser.quit()


def test_search_selene():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('second conflict commit').press_enter()