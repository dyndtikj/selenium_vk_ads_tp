from base import BaseCase
from ui.fixtures import *
from ui.pages.campaign_page import CampaignPage
import utuls


# @pytest.mark.skip()
class TestCampaign(BaseCase):
    @staticmethod
    def get_campaign_data(repo_root):
        return {
            'settings': {
                'site': 'vk.com',
                'budget': '100',
            },
            'group': {
                'search': 'Россия',
                'region': 188,
            },
            'advertisement': {
                'title': 'Тест',
                'short_description': 'Тестовое описание',
                'image_path': os.path.join(repo_root, 'files/img/advertisement.jpg'),
            }
        }

    @allure.story('Create campaign')
    def test_create_campaign(self, repo_root):
        campaign_page = CampaignPage(self.driver)
        data = self.get_campaign_data(repo_root)

        campaign_page.create_campaing(data)
        campaign_name = f'Кампания {utuls.get_today()}'
        ind, _ = campaign_page.find_ind_campaign_by_name(campaign_name)
        assert ind != -1

        campaign_page.delete_campaign(campaign_name)

    @allure.story('Delete campaign')
    def test_delete_campaign(self, repo_root):
        campaign_page = CampaignPage(self.driver)
        data = self.get_campaign_data(repo_root)

        campaign_page.create_campaing(data)
        campaign_name = f'Кампания {utuls.get_today()}'

        campaign_page.delete_campaign(campaign_name)
        self.driver.refresh()
        ind, _ = campaign_page.find_ind_campaign_by_name(campaign_name)
        assert ind == -1

