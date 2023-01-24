import time
from support.assertion import Assertion
from base_object.locators import Locators
from base_object.base import BaseObject
import os
import json

FULL_PATH = os.path.dirname(os.path.realpath(__file__))
PATH = os.path.dirname(FULL_PATH)
cred_path = str(PATH) + '/support/config.json'
creds_file = open(cred_path, 'rb')
creds = json.load(creds_file)

USERNAME = creds['correct_username']
PASSWORD = creds['correct_password']
INCORRECT_USERNAME = creds['incorrect_username']

class IndexPage(BaseObject, Assertion):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def login_flow(self):
        global USERNAME
        global PASSWORD
        self.to_send_keys(Locators.USER_NAME_FIELD, USERNAME)
        self.to_send_keys(Locators.PASSWORD_FIELD, PASSWORD)
        self.to_click(Locators.LOGIN_BTN)

    def input_correct_user_name(self):
        global USERNAME
        self.to_send_keys(Locators.USER_NAME_FIELD, USERNAME)

    def text_if_no_email(self):
        self.assertion_equal('E-mail address', self.get_text(Locators.ACTUAL_TEXT_WHEN_NO_EMAIL))

    def input_incorrect_user_name(self):
        self.to_send_keys(Locators.USER_NAME_FIELD, "greench@gmail.com")

    def input_correct_password(self):
        self.to_send_keys(Locators.PASSWORD_FIELD, "Agr47001ii")

    def input_incorrect_password(self):
        self.to_send_keys(Locators.PASSWORD_FIELD, "sauce")

    def click_login(self):
        self.to_click(Locators.LOGIN_BTN)

    def check_element_on_main(self):
        self.assertion_equal('Projects', self.get_text(Locators.ACTUAL_TEXT))

    def check_element_wrong_data(self):
        self.assertion_equal('Wrong email or password.', self.get_text(Locators.ACTUAL_TEXT_WRONG_DATA))

    def check_element_no_password_data(self):
        self.assertion_equal('Password is too week', self.get_text(Locators.ACTUAL_TEXT_WHEN_NO_PASSWORD))

    def forgot_password_click(self):
        self.to_click(Locators.FORGOT_PASSWORD)

    def input_email_restore_password_field(self):
        self.to_send_keys(Locators.FORGOT_PASSWORD_EMAIL_INPUT, "illia.demchuk@norse.digital")

    def click_restore_password(self):
        self.to_click(Locators.RESTORE_PASSWORD_BUTTON)


    def check_apply_email_forgot_pass(self):
        self.assertion_equal('The reset password link was sent to your email.',
                             self.get_text(Locators.ACTUAL_TEXT_APPLY_EMAIL_FOR_FORGOT_PASS))

    def click_on_sign_btn_on_forget_pass_page(self):
        self.to_click(Locators.SIGN_IN_BTN_ON_FG_PAGE)

    def check_txt_sign_in_on_log_page(self):
        self.assertion_equal(self.get_text(Locators.SIGN_IN_TXT_ON_MAIN), 'Sign in')






