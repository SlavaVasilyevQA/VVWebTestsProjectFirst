from pages.BasePage import BasePageHelper
from selenium.webdriver.common.by import By
import allure


class VKEcosystemPageLocators:
    VK_LOGO_BUTTON = (By.XPATH, '//header[@class="Header_header__vSdFG"]//a[@id="header-logo"]')


class VKEcosystemPageHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
        self.find_element(VKEcosystemPageLocators.VK_LOGO_BUTTON)
