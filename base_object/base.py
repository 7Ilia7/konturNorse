from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import math
import os
class BaseObject:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 600)

    def is_visible(self, locator):
        """

        :param locator:
        :return:
        """
        return self.wait.until(ec.visibility_of_element_located(locator))

    def is_click(self, locator):
        return self.wait.until(ec.element_to_be_clickable(locator))

    def get_text(self, locator):
        return self.is_visible(locator).text

    @staticmethod
    def assertion(actual, expected):
        assert actual == expected, f'Failed. Expected {expected}, but got {actual}'

    def to_click(self, locator):
        self.is_click(locator).click()

    def to_send_keys(self, locator, data):
        self.is_visible(locator).send_keys(data)

    def is_disappeared(self, locator, locator2):
        try:
            self.is_visible(locator)
        except NoSuchElementException:
            self.to_click(locator2)








