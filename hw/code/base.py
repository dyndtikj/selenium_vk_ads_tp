import allure
import pytest
from ui.pages.registration_page import RegistrationPage
from ui.pages.login_page import LoginPage
from ui.pages.settings_page import SettingsPage
from ui.pages.campaign_page import CampaignPage


CLICK_RETRY = 3

class BaseCase:
    driver = None
    authorize = True
    cabinet_created = True

    @allure.step("Setup")
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, logger, credentials):
        self.driver = driver
        self.config = config
        self.logger = logger

        if self.authorize:
            with allure.step("login"):
                login_page = LoginPage(self.driver)
                email, password = credentials

                registration_page = login_page.login(email, password)
                assert registration_page.is_opened()

        if self.cabinet_created:
            self.campaign_page = self.create_cabinet()
            self.campaign_page.close_onboarding()

        self.logger.debug('Initial setup completed')

    @allure.step("Teardown")
    @pytest.fixture(scope='function', autouse=True)
    def teardown(self):
        yield 

        if self.cabinet_created:
            self.delete_cabinet(self.campaign_page)

        self.logger.debug('Teardown completed')

    @allure.step("creating cabinet")
    def create_cabinet(self):
        registration_page = RegistrationPage(self.driver)
        
        data = {'email': 'test@mail.ru'}
        campaign_page = registration_page.create_cabinet(data)
        
        return campaign_page

    @allure.step("deleting cabinet")
    def delete_cabinet(self, campaign_page):
        campaign_page.move_to('settings')

        settings_page = SettingsPage(self.driver)
        settings_page.delete_account()