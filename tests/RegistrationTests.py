from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPageHelper
from pages.RegistrationPage import RegistrationPageHelperHelper
import allure

BASE_URL = 'https://ok.ru/'


@allure.suite('Проверка регистрации пользователя')
@allure.title('Проверка перехода на регистрацию и сверка выбранной страны с кодом телефона')
def test_registration_random_country(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    login_page = LoginPageHelper(browser)
    login_page.click_registration()
    registration_page = RegistrationPageHelperHelper(browser)
    selected_country_code = registration_page.select_random_country()
    actual_country_code = registration_page.get_phone_field_value()
    assert selected_country_code == actual_country_code
