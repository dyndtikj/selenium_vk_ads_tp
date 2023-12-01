from ui.locators import basic_locators
from ui.pages.base_page import BasePageAuthorized


class SitesPage(BasePageAuthorized):
    url = r'^https:\/\/ads\.vk\.com\/hq\/pixels.*$'

    locators = basic_locators.SitesPageLocators
