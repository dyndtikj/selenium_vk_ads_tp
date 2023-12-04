import allure
from ui.locators import basic_locators
from ui.pages.base_page import BasePage


class MonetizationPage(BasePage):
    url = r'^https:\/\/ads\.vk\.com\/partner.*$'

    locators = basic_locators.MonetizationPageLocators

    # def is_opened(self, timeout=15):
    #     Set s= self.driver.window_handles
    #
    #     while (ite.hasNext())
    #         {
    #             String
    #         popupHandle = ite.next().toString();
    #         if (!popupHandle.contains(mwh))
    #         {
    #         driver.switchTo().window(popupHandle);
    #         / ** /here you can perform operation in pop-up window **
    #         // After finished your operation in pop-up just select the main window again
    #         driver.switchTo().window(mwh);
    #         }
    #         }