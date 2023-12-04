import allure
from ui.locators import basic_locators
from ui.pages.base_page import BasePage, NoNavbarSection
from selenium.webdriver.common.action_chains import ActionChains



class MainPage(BasePage):
    url = r'^https:\/\/ads\.vk\.com\/$'

    locators = basic_locators.MainPageLocators
    navbar = {
        'logo': locators.LOGO_LOCATOR,
        'news': locators.NEWS_LOCATOR,
        'cases': locators.CASES_LOCATOR,
        'ideas_forum': locators.FORUM_LOCATOR,
        'monetization': locators.MONETIZATION_LOCATOR,
        'help': locators.HELP_LOCATOR,
        'cabinet': locators.CABINET_LOCATOR,
    }

    def accept_cookie(self):
        self.click(self.locators.ACCEPT_COOKIE_LOCATOR)

    def move_to(self, section_name):
        locator = self.navbar.get(section_name, None)

        if locator is not None:
            self.click(locator)
            handles_len = len(self.driver.window_handles)
            if handles_len > 1:
                self.driver.switch_to.window(self.driver.window_handles[-1])
        else:
            raise NoNavbarSection

    def open_footer_section(self, ind):
        self.scroll_down()
        sections = self.find_list(self.locators.FOOTER_ITEM_LOCATOR)
        sections[ind].click()
