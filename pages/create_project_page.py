from base_object.locators import CreateProjectsLocator
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
        time.sleep(2)

    def click_layer_thikness(self):
        self.to_click(CreateProjectsLocator.LAYER_THIKNESS)

    def input_layer_name(self):
        self.to_send_keys(CreateProjectsLocator.INPUT_LAYER_NAME, 'BaseThiknessLayer')

    def click_top_layer_dropdown(self):
        self.to_click(CreateProjectsLocator.BTN_TOP)
        time.sleep(2)