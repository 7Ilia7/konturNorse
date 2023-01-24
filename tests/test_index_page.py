import allure
import pytest

@pytest.mark.ui
@pytest.mark.regression
def test_correct_login(index_page):
    index_page.input_correct_user_name()
    index_page.input_correct_password()
    index_page.click_login()
    index_page.check_element_on_main()

@pytest.mark.ui
@pytest.mark.regression
def test_incorrect_login(index_page):
    index_page.input_incorrect_user_name()
    index_page.input_correct_password()
    index_page.click_login()
    index_page.check_element_wrong_data()

@pytest.mark.ui
@pytest.mark.regression
def test_only_password_data(index_page):
    index_page.input_correct_password()
    index_page.click_login()
    index_page.text_if_no_email()

@pytest.mark.ui
def test_only_email_data(index_page):
    index_page.input_correct_user_name()
    index_page.click_login()
    index_page.check_element_no_password_data()

@pytest.mark.ui
@pytest.mark.regression
def test_forgot_password(index_page):
    index_page.forgot_password_click()
    index_page.input_email_restore_password_field()
    index_page.click_restore_password()
    index_page.check_apply_email_forgot_pass()

@pytest.mark.ui
@pytest.mark.regression
def test_signin_btn_on_forget_password_page(index_page):
    index_page.forgot_password_click()
    index_page.click_on_sign_btn_on_forget_pass_page()
    index_page.check_txt_sign_in_on_log_page()






