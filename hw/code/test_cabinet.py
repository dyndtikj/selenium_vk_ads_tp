from base import BaseCase
from ui.fixtures import *
from ui.pages.login_page import LoginPage
from ui.pages.campaign_page import CampaignPage
from ui.pages.audience_page import AudiencePage
from ui.pages.budget_page import BudgetPage
from ui.pages.ecomm_page import ECommPage
from ui.pages.sites_page import SitesPage
from ui.pages.mobapps_page import MobAppsPage
from ui.pages.leadads_page import LeadAdsPage
from ui.pages.settings_page import SettingsPage


# @pytest.mark.skip()
class TestCabinet(BaseCase):
    cabinet_created = False

    @allure.story('Create Cabinet')
    def test_create_cabinet(self):
        campaign_page = self.create_cabinet()
        assert campaign_page.is_opened()
        self.delete_cabinet(campaign_page)

    @allure.story('Delete Cabinet')
    def test_delete_cabinet(self):
        campaign_page = self.create_cabinet()
        self.delete_cabinet(campaign_page)
        assert LoginPage(self.driver).is_opened()


# @pytest.mark.skip()
class TestCabinetNavigation(BaseCase):
    @allure.story('Navigation')
    @pytest.mark.parametrize(
        'to_section, page',
        [
            pytest.param('campaigns', CampaignPage),
            pytest.param('audience', AudiencePage),
            pytest.param('budget', BudgetPage),
            pytest.param('ecomm', ECommPage),
            pytest.param('sites', SitesPage),
            pytest.param('mobapps', MobAppsPage),
            pytest.param('leadads', LeadAdsPage),
            pytest.param('settings', SettingsPage),
        ]
    )
    def test_navigation(self, to_section, page):
        campaign_page = CampaignPage(self.driver)
        campaign_page.move_to(to_section)
        assert page(self.driver).is_opened()
