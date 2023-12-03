from selenium.webdriver.common.by import By

from base import BaseCase
from ui.fixtures import *
from ui.pages.main_page import MainPage
from ui.pages.insights_page import InsightsPage
from ui.pages.news_page_footer import NewsPageFooter
from ui.pages.events_page import EventsPage
from ui.pages.experts_page import ExpertPage
from ui.pages.cases_page import CasesPage
from ui.pages.documents_page import DocumentsPage
from ui.pages.monetization_footer_page import MonetizationFooterPage


# @pytest.mark.skip()
class TestFooterNavigation(BaseCase):
    cabinet_created = False
    authorize = False
    accept_cookie = True

    @allure.story('Navigation')
    @pytest.mark.parametrize(
        'section_idx, page',
        [
            # pytest.param(0, NewsPageFooter),
            pytest.param(1, ExpertPage),
            pytest.param(2, InsightsPage),
            # pytest.param(3, CasesPage),
            pytest.param(4, EventsPage),
            pytest.param(6, DocumentsPage),
            # pytest.param(7, MonetizationFooterPage),
        ]
    )
    def test_footer_navigation(self, section_idx, page):
        main_page = MainPage(self.driver)
        main_page.open_footer_section(section_idx)
        assert page(self.driver).is_opened()
