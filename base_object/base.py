from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from support.logger import log_method
import logging as log
import math
import os
class BaseObject:
    log = log_method(logLevel=log.INFO)
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 600)

    def is_visible(self, locator):
        """
        to find visible element
        :param locator: is responsible for element
        :return: visible element
        """
        self.log.info(f"{locator} is visible")
        return self.wait.until(ec.visibility_of_element_located(locator))


    def is_click(self, locator):
        """
        element clickability indicator
        :param locator: is responsible for element
        :return: clickable state of an element
        """
        self.log.info(f"{locator} is clickable")
        return self.wait.until(ec.element_to_be_clickable(locator))

    def get_text(self, locator):
        """
        get text from element
        :param locator: is responsible for element
        :return: text from element
        """
        self.log.info(f"get text from {locator}")
        return self.is_visible(locator).text

    @staticmethod
    def assertion(actual, expected):
        """
        Comparison of actual and expected result
        :param actual: the result that is now
        :param expected: the result we want to get
        :return: compliance or non-compliance of the actual result with the expected
        """
        assert actual == expected, f'Failed. Expected {expected}, but got {actual}'

    def to_click(self, locator):
        """
        to click on visible element
        :param locator: is responsible for element
        :return: Clicking on an element
        """
        self.log.info(f"do click on {locator}")
        self.is_click(locator).click()

    def to_send_keys(self, locator, data):
        """
        Send values like "greench" or "123"
        :param locator: is responsible for element
        :param data: values
        :return: fills the input field with data
        """
        self.log.info(f"send keys or data on {locator}")
        self.is_visible(locator).send_keys(data)

    def is_disappeared(self, locator, locator2):
        """
        :param locator:
        :param locator2:
        :return:
        """
        try:
            self.is_visible(locator)
        except NoSuchElementException:
            self.to_click(locator2)








