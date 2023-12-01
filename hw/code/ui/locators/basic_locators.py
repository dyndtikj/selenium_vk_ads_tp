from selenium.webdriver.common.by import By


class BasePageLocators:
    pass


class LoginPageLocators:
    TRIGGER_LOGIN_LOCATOR = (By.XPATH, "//a[contains(@class, 'ButtonCabinet')]")
    OAUTH_MAIL_LOCATOR = (By.XPATH, "//button[contains(@data-test-id, 'oAuthService_mail_ru')]")

    EMAIL_LOCATOR = (By.NAME, "username")
    ENTER_PASSWORD_LOCATOR = (By.XPATH, "//button[contains(@data-test-id, 'next-button')]")
    PASSWORD_LOCATOR = (By.NAME, "password")
    SUBMIT_LOCATOR = (By.XPATH, "//button[contains(@data-test-id, 'submit-button')]")

    RECAPTCHA_BTN_LOCATOR = (By.XPATH, "//button[contains(@data-test-id, 'recaptcha-inter-next')]")


class RegistrationPageLocators:
    CREATE_CABINET_LOCATOR = (By.ID, "click-createNewButton")
    EMAIL_LOCATOR = (By.NAME, "email")
    SUBMIT_LOCATOR = (By.XPATH, "//button[contains(@data-testid, 'create-button')]")


class BasePageAuthorizedLocators:
    CAMPAIGN_LOCATOR = (By.XPATH, "//a[contains(@data-entityid, 'dashboardV2')]")
    AUDIENCE_LOCATOR = (By.XPATH, "//a[contains(@data-entityid, 'audience')]")
    BUDGET_LOCATOR = (By.XPATH, "//a[contains(@data-entityid, 'budget')]")
    ECOMM_LOCATOR = (By.XPATH, "//a[contains(@data-entityid, 'catalogs')]")
    SITE_LOCATOR = (By.XPATH, "//a[contains(@data-entityid, 'pixels')]")
    MOBAPP_LOCATOR = (By.XPATH, "//a[contains(@data-entityid, 'mobApps')]")
    LEADAD_LOCATOR = (By.XPATH, "//a[contains(@data-entityid, 'leadads')]")
    SETTINGS_LOCATOR = (By.XPATH, "//a[contains(@data-entityid, 'settings')]")


class CampaignPageLocators:
    ONBOARDING_LOCATOR = (By.XPATH, "//div[contains(@class, 'ModalManagerPage_modalContent')]")
    ONBOARDING_CLOSE_LOCATOR = (By.XPATH, "//div[contains(@class, 'vkuiModalDismissButton')]")

    START_CREATING_CAMPAIGN = (By.XPATH, "//a[contains(@data-testid, 'create-button')]")
    CAMPAIGN_LOCATOR = (By.XPATH, "//button[contains(@class, 'nameCellContent_link_')]")
    CHECHBOX_CAMPAIGN_LOCATOR = (By.XPATH, "//div[contains(@class, 'vkuiCheckbox__icon--off')]")
    OPTIONS_LOCATOR = (By.XPATH, "//span[contains(@data-testid, 'select-options')]")
    SELECT_OPTIONS_LOCATOR = (By.NAME, "actionType")


class CampaignSettingsPageLocators:
    SITE_LOCATOR = (By.XPATH, "//div[contains(@data-id, 'site_conversions')]")
    SITE_MODAL_LOCATOR = (By.XPATH, "//div[contains(@data-name, 'object')]")
    SITE_FIELD_LOCATOR = (By.XPATH, "//input[contains(@class, 'vkuiInput__el')]")
    BUDGET_MODAL_LOCATOR = (By.XPATH, "//div[contains(@data-name, 'budget')]")
    BUDGET_FIELD_LOCATOR = (By.XPATH, "//input[contains(@data-testid, 'targeting-not-set')]")
    FOOTER_LOCATOR = (By.XPATH, "//div[contains(@class, 'CreateFooter_footer_')]")
    CONTINUE_LOCATOR = (By.XPATH, "//button[contains(@class, 'vkuiButton--mode-primary')]")


class GroupPageLocators:
    SEARCH_LOCATOR = (By.XPATH, "//input[contains(@class, 'vkuiSearch__input')]")
    CHECKBOX_LOCATOR = (By.XPATH, "//div[contains(@data-value, '{}')]")
    CONTINUE_LOCATOR = (By.XPATH, "//button[contains(@class, 'vkuiButton--mode-primary')]")


class AdvertisementPageLocators:
    TITLE_LOCATOR = (By.NAME, "заголовок, макс. 40 символов")
    SHORT_DESCRIPTION_LOCATOR = (By.NAME, "заголовок, макс. 90 символов")
    IMAGE_INPUT_LOCATOR = (By.XPATH, "//input[contains(@class, 'vkuiFile__input')]")
    PREVIEW_LOCATOR = (By.XPATH, "//img[contains(@class, 'FirstTemplate_firstImage') and contains(@src, 'r.mradx.net')]")

    SUBMIT_LOCATOR = (By.XPATH, "//button[contains(@class, 'vkuiButton--mode-primary')]")


class AudiencePageLocators(BasePageLocators):
    pass


class BudgetPageLocators(BasePageLocators):
    pass


class ECommPageLocators(BasePageLocators):
    pass


class SitesPageLocators(BasePageLocators):
    pass


class MobAppsPageLocators(BasePageLocators):
    pass


class LeadAdsPageLocators(BasePageLocators):
    pass


class SettingsLocators(BasePageLocators):
    DELETE_ACCOUNT_LOCATOR = (By.XPATH, "//button[contains(@class, 'DeleteAccount_button')]")
    MODAL_ACTIONS_DELETE_ACCOUNT = (By.XPATH, "//div[contains(@class, 'DeleteAccountConfirmModal_actions')]")
    CONFIRM_DELETE_ACCOUNT = (By.XPATH, "//button[contains(@class, 'vkuiButton--mode-primary') and contains(@class, 'vkuiButton--appearance-negative')]")
