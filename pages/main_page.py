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


    def click_on_projects_btn_menu(self):
        self.to_click(MainPageLocators.PROJECTS_BTN)

    def click_om_list_projects_display(self):
        self.to_click(MainPageLocators.PROJECTS_BTN_LIST)

    def click_om_tile_projects_display(self):
        self.to_click(MainPageLocators.PROJECTS_BTN_TILE)

    def click_on_btn_start_new_project(self):
        self.to_click(MainPageLocators.START_NEW_PROJECTS_BTN)

