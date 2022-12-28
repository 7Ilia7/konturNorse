from base_object.locators import MainPageLocators
from base_object.base import BaseObject
class MainPage(BaseObject):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_on_profile_btn(self):
        self.to_click(MainPageLocators.PROFILE_BTN)

    def click_on_logo(self):
        self.to_click(MainPageLocators.LOGO_BTN)

    def click_on_user_management(self):
        self.is_click(MainPageLocators.USER_MANAGEMENT_BTN)


    def click_on_data_package_menu(self):
        self.to_click(MainPageLocators.DATA_PACKAGE_BTN)

    def check_in_data_package_menu(self):
        self.assertion(self.get_text(MainPageLocators.DATA_PACKAGE_TXT), 'Data Packages')


    def click_on_projects_btn_menu(self):
        self.to_click(MainPageLocators.PROJECTS_BTN)

    def click_om_list_projects_display(self):
        self.to_click(MainPageLocators.PROJECTS_BTN_LIST)

    def click_om_tile_projects_display(self):
        self.to_click(MainPageLocators.PROJECTS_BTN_TILE)

    def click_on_btn_start_new_project(self):
        self.to_click(MainPageLocators.START_NEW_PROJECTS_BTN)

    def check_that_we_not_have_any_project(self):
        self.assertion(self.get_text(MainPageLocators.TEXT_WHEN_WE_HAVE_ANY_PROJECT), 'Click on the button below to get started')

    def check_no_processing(self):
        self.is_disappeared(MainPageLocators.PROCESSING, MainPageLocators.DELETE_FIRST_PROJECT_IN_LIST)

