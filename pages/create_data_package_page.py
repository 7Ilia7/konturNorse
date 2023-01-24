from support.assertion import Assertion
from base_object.locators import DataPackagePageLocators
from base_object.base import BaseObject
import os
class CreateDataPackagePage(BaseObject,Assertion):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    FULL_PATH = os.path.abspath(os.path.dirname(__file__))
    PATH = os.path.dirname(FULL_PATH)
    two_hundred_asphalt_file = str(PATH) + '/support/asphalt_combined.txt'


    def click_create_data_package(self):
        self.to_click(DataPackagePageLocators.CREATE_DATA_PACKAGE_BUTTON)
    def input_data_package_name(self):
        self.to_send_keys(DataPackagePageLocators.NAME_DATA_PACKAGE, "200mTestQa")

    def click_add_new_data_type(self):
        self.to_click(DataPackagePageLocators.ADD_NEW_DATA_TYPE)

    def click_layer_thickness_drop_down(self):
        self.to_click(DataPackagePageLocators.CLICK_LATER_THICKNESS_DROP_DOWN)

    def click_create_new_interface_button(self):
        self.to_click(DataPackagePageLocators.CREATE_NEW_INTERFACE_BUTTON)

    def click_on_interface_drop_down_asphalt(self):
        self.to_click(DataPackagePageLocators.CLICK_INTERFACE_TYPE_DROP_DOWN)
        self.to_click(DataPackagePageLocators.CHOOSE_ASPHALT_INTERFACE_TYPE)

    def click_asphalt_button_drop_dawn(self):
        self.to_click(DataPackagePageLocators.CLICK_ASPHALT_BUTTON_DROP_DOWN)

    def click_to_upload_new_file_to_this_interface_asphalt_200m(self):
        FULL_PATH = os.path.abspath(os.path.dirname(__file__))
        PATH = os.path.dirname(FULL_PATH)
        two_hundred_asphalt_file = str(PATH) + '/support/asphalt_combined.txt'
        self.to_send_keys(DataPackagePageLocators.UPLOAD_NEW_FILE_TO_THIS_INTERFACE, two_hundred_asphalt_file)
