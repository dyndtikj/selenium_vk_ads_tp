import allure
from ui.locators import basic_locators
from ui.pages.base_page import BasePage


class HelpPage(BasePage):
    url = r'^https:\/\/ads\.vk\.com\/help.*$'

    locators = basic_locators.HelpPageLocators
