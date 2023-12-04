from selenium.webdriver.common.by import By

from base import BaseCase
from ui.fixtures import *
from ui.pages.main_page import MainPage
from ui.pages.insights_page import InsightsPage


# @pytest.mark.skip()
class TestFooterNavigation(BaseCase):
    cabinet_created = False
    authorize = False
    accept_cookie = True

    @allure.story('Navigation')
    @pytest.mark.parametrize(
        'section_idx, page',
        [
            pytest.param(2, InsightsPage),
        ]
    )
    def test_footer_navigation(self, section_idx, page):
        main_page = MainPage(self.driver)
        main_page.open_footer_section(section_idx)
        assert page(self.driver).is_opened()