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

    def click_to_upload_new_file_to_this_interface_asphalt_200m(self):
        FULL_PATH = os.path.abspath(os.path.dirname(__file__))
        PATH = os.path.dirname(FULL_PATH)
        two_hundred_asphalt_file = str(PATH) + '/support/asphalt_combinedd.txt'
        self.to_send_keys(DataPackagePageLocators.UPLOAD_DATA_PACKAGE_FILE, two_hundred_asphalt_file)
