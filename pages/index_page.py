from base_object.locators import Locators
from base_object.base import BaseObject



class IndexPage(BaseObject):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def input_correct_user_name(self):
        self.to_send_keys(Locators.USER_NAME_FIELD, "illia.demchuk@norse.digital")

    def text_if_no_email(self):
        self.assertion(self.get_text(Locators.ACTUAL_TEXT_WHEN_NO_EMAIL),
                       'E-mail address')

    def input_incorrect_user_name(self):
        self.to_send_keys(Locators.USER_NAME_FIELD, "greench@gmail.com")

    def input_correct_password(self):
        self.to_send_keys(Locators.PASSWORD_FIELD, "Agr47001ii")

    def input_incorrect_password(self):
        self.to_send_keys(Locators.PASSWORD_FIELD, "sauce")

    def click_login(self):
        self.to_click(Locators.LOGIN_BTN)

    def check_element_on_main(self):
        self.assertion(self.get_text(Locators.ACTUAL_TEXT),
                       'Projects')

    def check_element_wrong_data(self):
        self.assertion(self.get_text(Locators.ACTUAL_TEXT_WRONG_DATA),
                       'Wrong email or password.')

    def check_element_no_password_data(self):
        self.assertion(self.get_text(Locators.ACTUAL_TEXT_WHEN_NO_PASSWORD),
                       'Password is too week')

    def forgot_password_click(self):
        self.to_click(Locators.FORGOT_PASSWORD)

    def input_email_restore_password_field(self):
        self.to_send_keys(Locators.FORGOT_PASSWORD_EMAIL_INPUT, "illia.demchuk@norse.digital")

    def click_restore_password(self):
        self.to_click(Locators.RESTORE_PASSWORD_BUTTON)


    def check_apply_email_forgot_pass(self):
        self.assertion(self.get_text(Locators.ACTUAL_TEXT_APPLY_EMAIL_FOR_FORGOT_PASS),
                       'The reset password link was sent to your email.')

    def click_on_sign_btn_on_forget_pass_page(self):
        self.to_click(Locators.SIGN_IN_BTN_ON_FG_PAGE)

    def check_txt_sign_in_on_log_page(self):
        self.assertion(self.get_text(Locators.SIGN_IN_TXT_ON_MAIN), 'Sign in')






