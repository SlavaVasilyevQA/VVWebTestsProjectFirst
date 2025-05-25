from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPageHelper
import allure

BASE_URL = 'https://ok.ru/'
EMPTY_LOGIN_ERROR = 'Введите логин'
EMPTY_PASSWORD_ERROR = 'Введите пароль'


@allure.suite('Проверка формы авторизации')
@allure.title('Проверка ошибки при пустой форме авторизации')
def test_empty_login_and_password(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    login_page = LoginPageHelper(browser)
    login_page.click_login()
    assert login_page.get_error_text() == EMPTY_LOGIN_ERROR


@allure.suite('Проверка формы авторизации')
@allure.title('Проверка ошибки при вводе логина без пароля на форме авторизации')
def test_input_login_without_password(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    login_page = LoginPageHelper(browser)
    login_page.type_login("просто текст например этот")
    login_page.click_login()
    assert login_page.get_error_text() == EMPTY_PASSWORD_ERROR
