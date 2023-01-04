import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Chrome_options
import allure
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.index_page import IndexPage
from pages.main_page import MainPage
from pages.create_project_page import CreateProjectPage

@pytest.fixture
def get_chrome_options():
    """
    Options with which the browser is launched (maximum screen, etc.)
    :return: Certain Options
    """
    options = Chrome_options()
    options.add_argument('chrome')
    options.add_argument('--start-maximized')
    return options

@pytest.fixture
def get_webdriver(get_chrome_options):
    """
    launching a browser with certain options
    :param get_chrome_options: a set of options for our browser
    :return: launching a browser
    """
    options = get_chrome_options
    driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    return driver

@pytest.fixture(scope='function')
def setup(get_webdriver):
    """
    launching the webdriver and going to the page defined in the "url" variable
    :param get_webdriver:
    :return:
    """
    driver = get_webdriver
    url = 'https://customer.dev.kontur.tech/'
    driver.get(url)
    yield driver
    driver.quit()

@pytest.fixture
def index_page(setup):
    """
    Class methods for working with index_page page elements
    :param setup: Launching our browser with presets
    :return: makes our class methods abstract
    """
    yield IndexPage(setup)

@pytest.fixture
def main_page(setup):
    """
    Class methods for working with main_page page elements
    :param setup: Launching our browser with presets
    :return: makes our class methods abstract
    """
    yield MainPage(setup)

@pytest.fixture
def create_project_page(setup):
    """
    Class methods for working with create_project_page elements
    :param setup: Launching our browser with presets
    :return: makes our class methods abstract
    """
    yield CreateProjectPage(setup)



















# @pytest.hookimpl(hookwrapper=True, tryfirst=True)
# def pytest_runtest_makereport(item):
#     outcome = yield
#     rep = outcome.get_result()
#     marker = item.get_closest_marker("ui")
#     if marker:
#         if rep.when == "call" and rep.failed:
#             try:
#                 allure.attach(item.instance.driver.get_screenshot_as_png(),
#                               name=item.name,
#                               attachment_type=allure.attachment_type.PNG)
#             except Exception as e:
#                 print(e)