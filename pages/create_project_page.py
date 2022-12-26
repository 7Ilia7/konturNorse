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

    def input_project_name_14km_all_tracker(self):
        self.to_send_keys(CreateProjectsLocator.PROJECT_NAME_FIELD, "14km_all_tracker")

    def choose_data_package(self):
        self.to_click(CreateProjectsLocator.CHOOSE_DATA_PACKAGE_200M)

    def choose_data_package_14km(self):
        self.to_click(CreateProjectsLocator.CHOOSE_DATA_PACKAGE_14KM)

    def btn_next(self):
        self.to_click(CreateProjectsLocator.BTN_NEXT)

    def btn_start_build_project(self):
        self.to_click(CreateProjectsLocator.BTN_START_BUILDING_PROJ)

    def add_more_tracker_btn(self):
        self.to_click(CreateProjectsLocator.ADD_MORE_TRACKER_BTN)

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

    def check_200m_project_was_created(self):
        self.assertion(self.get_text(MainPageLocators.FIND_200M_PROJECT), "200mTest")

    def delete_first_project_in_list(self):
        self.to_click(MainPageLocators.DELETE_FIRST_PROJECT_IN_LIST)
        self.to_click(MainPageLocators.DELETE_YES)

# add delamination layer, when we create project

    def click_delam_layer(self):
        self.to_click(CreateProjectsLocator.DELAM)

    def input_name_delam_layer_field(self):
        self.to_send_keys(CreateProjectsLocator.NAME_INPUT_FIELD_DELAM_OR_CRACK, 'Delam Layer')

    def choose_asphalt_layer(self):
        self.to_click(CreateProjectsLocator.CHECK_ASPH_BASE_BOTTOM)

    def choose_surface_layer(self):
        self.to_click(CreateProjectsLocator.CHECK_SURFACE_ASPH_BOTTOM)

    def add_selected_tracker_delam(self):
        self.to_click(CreateProjectsLocator.ADD_SELECTED_TRACKER_BTN_DELAM)

#  create crack layer

    def click_add_crack_layer(self):
        self.to_click(CreateProjectsLocator.CRACK)

    def input_name_crack_layer(self):
        self.to_send_keys(CreateProjectsLocator.NAME_INPUT_FIELD_DELAM_OR_CRACK, 'Crack layer')

    def check_box_asphalt_layer(self):
        self.to_click(CreateProjectsLocator.CHECK_ASPHALT_BOTTOM_CRACK)

    def check_box_base_bottom_crack(self):
        self.to_click(CreateProjectsLocator.CHECK_ASPHALT_BOTTOM_CRACK)

    def check_box_surface_bottom_layer(self):
        self.to_click(CreateProjectsLocator.CHECK_SURFACE_CRACK)

