from ui.pages.main_page import MainPage
from ui.locators import basic_locators


class MonetizationFooterPage(MainPage):
    url = r'^https:\/\/ads\.vk\.com\/partner.*$'

    locators = basic_locators.MonetizationFooterPageLocators
