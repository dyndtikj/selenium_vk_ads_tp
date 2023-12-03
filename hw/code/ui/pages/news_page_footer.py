from ui.pages.main_page import MainPage
from ui.locators import basic_locators


class NewsPageFooter(MainPage):
    url = r'https:\/\/ads\.vk\.com\/news.*$'

    locators = basic_locators.NewsPageLocatorsFooter
