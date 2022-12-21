from base_object.locators import MainPageLocators
from base_object.base import BaseObject
import time
class CreateProjectPage(BaseObject):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # def
