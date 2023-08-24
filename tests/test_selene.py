from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_azalia():
    browser.open("https://azalianow.ru/")

    s("[class^='MobileAppAdvertModal_modalCloseBtn']").click()
    # s("[class^=SearchBar_wrapper__]").click
    s("[inputmode=search]").send_keys("Хризантема").press_enter()
    s(by.partial_text("Хризантема")).should(be.visible)
