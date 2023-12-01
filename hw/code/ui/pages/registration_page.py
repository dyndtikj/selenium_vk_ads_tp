import allure
from ui.locators import basic_locators
from ui.pages.base_page import BasePageAuthorized
from ui.pages.campaign_page import CampaignPage


class RegistrationPage(BasePageAuthorized):
    url = r'^https:\/\/ads\.vk\.com\/hq\/registration.*$'

    locators = basic_locators.RegistrationPageLocators

    @allure.step("Creating cabinet")
    def create_cabinet(self, data):
        self.click(self.locators.CREATE_CABINET_LOCATOR)
        self.fill_field(self.locators.EMAIL_LOCATOR, data['email'])
        self.click(self.locators.SUBMIT_LOCATOR)

        return CampaignPage(self.driver)

