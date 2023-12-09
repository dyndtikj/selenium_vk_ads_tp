from ui.locators import basic_locators
from ui.pages.base_page import BasePage


class HelpPage(BasePage):
    url = r'^https:\/\/ads\.vk\.com\/help.*$'

    locators = basic_locators.HelpPageLocators

    def open_help_section(self, ind):
        sections = self.find_list(self.locators.HELP_ITEMS_LOCATOR)
        sections[ind].click()
