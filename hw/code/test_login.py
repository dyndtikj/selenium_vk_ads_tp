from base import BaseCase
from ui.fixtures import *
from ui.pages.login_page import LoginPage


# @pytest.mark.skip()
class TestLogin(BaseCase):
    authorize = False
    cabinet_created = False

    @allure.story('Login')
    def test_login(self, credentials):
        login_page = LoginPage(self.driver)
        email, password = credentials

        registration_page = login_page.login(email, password)
        assert registration_page.is_opened()
