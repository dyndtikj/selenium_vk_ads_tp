from ui.locators import basic_locators
from ui.pages.base_page import BasePageAuthorized


class AudiencePage(BasePageAuthorized):
    url = r'^https:\/\/ads\.vk\.com\/hq\/audience.*$'

    locators = basic_locators.AudiencePageLocators
