from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.HelpPage import HelpPageHelper, HelpPageLocators
from pages.AdvertisementCabinetHelp import AdvertisementCabinetHelpHelper
import allure

BASE_URL = 'https://ok.ru/help'


@allure.suite('Проверка страницы помощи')
@allure.title('Проверка скролла на странице, выполняем поиск элемента и выполняем клик')
def test_help_page_scroll_to_item_and_click(browser):
    BasePage(browser).get_url(BASE_URL)
    help_page = HelpPageHelper(browser)
    help_page.scroll_to_item(HelpPageLocators.ADVERTISEMENT_CABINET)
    AdvertisementCabinetHelpHelper(browser)
