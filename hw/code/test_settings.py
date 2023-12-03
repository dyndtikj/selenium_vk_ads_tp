from base import BaseCase
from ui.fixtures import *
from ui.pages.campaign_page import CampaignPage
from ui.pages.settings_page import SettingsPage, SettingsNotificationsPage, SettingsAccessPage, SettingsLogsPage


# @pytest.mark.skip()
class TestSettings(BaseCase):
    @staticmethod
    def get_account_data():
        return {
            'phone': '+79000000000', 
            'fio': 'Тестов Тест Тестович',
            'inn': '112329166348'
        }

    @allure.story('Edit account info')
    def test_edit_account_info(self):
        campaign_page = CampaignPage(self.driver)
        campaign_page.move_to('settings')
        settings_page = SettingsPage(self.driver)
        data = self.get_account_data()

        settings_page.edit_account_info(data)
        self.driver.refresh()
        assert data == settings_page.get_account_info()

    @pytest.mark.parametrize(
        'to_section, page',
        [
            pytest.param('common', SettingsPage),
            pytest.param('notifications', SettingsNotificationsPage),
            pytest.param('access', SettingsAccessPage),
            pytest.param('logs', SettingsLogsPage),
        ]
    )
    @allure.story('Open section {to_section}')
    def test_open_section(self, to_section, page):
        campaign_page = CampaignPage(self.driver)
        campaign_page.move_to('settings')
        settings_page = SettingsPage(self.driver)
        settings_page.open_section(to_section)
        assert page(self.driver).is_opened()