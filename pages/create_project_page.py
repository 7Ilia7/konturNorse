from base_object.locators import CreateProjectsLocator
from base_object.locators import MainPageLocators
from base_object.base import BaseObject
import time
class CreateProjectPage(BaseObject):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def input_project_name(self):
        self.to_send_keys(CreateProjectsLocator.PROJECT_NAME_FIELD, "200mTest")

    def choose_data_package(self):
        self.to_click(CreateProjectsLocator.CHOOSE_DATA_PACKAGE_200M)

    def btn_next(self):
        self.to_click(CreateProjectsLocator.BTN_NEXT)

    def btn_start_build_project(self):
        self.to_click(CreateProjectsLocator.BTN_START_BUILDING_PROJ)

    def click_layer_thikness(self):
        self.to_click(CreateProjectsLocator.LAYER_THIKNESS)

    def input_layer_name(self):
        self.to_send_keys(CreateProjectsLocator.INPUT_LAYER_NAME, 'BaseThiknessLayer')

    def click_top_layer_dropdown(self):
        self.to_click(CreateProjectsLocator.BTN_TOP)

    def click_asphalt_bottom(self):
        self.to_click(CreateProjectsLocator.ASPHALT_BOTTOM)

    def click_bottom_layer_dropdown(self):
        self.to_click(CreateProjectsLocator.BTN_BOTTOM)

    def click_bottom_bottom_layer(self):
        self.to_click(CreateProjectsLocator.BASE_BOTTOM)

    def add_selected_tracker(self):
        self.to_click(CreateProjectsLocator.ADD_SELECTED_TRACKER_BTN)

    def create_project_btn(self):
        self.to_click(CreateProjectsLocator.CREATE_PROJECT_BTN)
        time.sleep(20)

    def delete_first_project_in_list(self):
        self.to_click(MainPageLocators.DELETE_FIRST_PROJECT_IN_LIST)
        self.to_click(MainPageLocators.DELETE_YES)
        time.sleep(10)


    # def check_200m_project_was_created(self):
    #     self.assertion(self.get_text(MainPageLocators.FIND_200M_PROJECT), '200mTest')
    #     time.sleep(20)


