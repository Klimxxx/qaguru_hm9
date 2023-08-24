from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
import allure

def test_azalia_search_dinamyc_steps():
    with allure.step("Открываем главную страницу сайта"):
        browser.open("https://azalianow.ru/")

    with allure.step("Закрываем рекламное окно моб.приложения"):
        s("[class^='MobileAppAdvertModal_modalCloseBtn']").click()

    with allure.step("Ищем в поиске Хризантему"):
        s("[inputmode=search]").send_keys("Хризантема").press_enter()

    with allure.step("Проверяем наличие текста Хризантема в результатах выдачи"):
        s(by.partial_text("Хризантема")).should(be.visible)
