from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.LoginPage import LoginPageHelper
from pages.RecoveryPage import RecoveryPageHelper
import allure

BASE_URL = 'https://ok.ru/'
LOGIN_TEXT = 'email'
PASSWORD_TEXT = '1'


@allure.suite('Проверка восстановления пользователя')
@allure.title('Проверка перехода к восстановлению после нескольких неудачных попыток авторизации')
def test_go_to_recovery_after_many_fails(browser):
    BasePage(browser).get_url(BASE_URL)
    login_page = LoginPageHelper(browser)
    login_page.type_login(LOGIN_TEXT)
    for i in range(3):
        login_page.type_password(PASSWORD_TEXT)
        login_page.click_login()
    login_page.click_recovery()
    RecoveryPageHelper(browser)
