import pytest

@pytest.mark.regression
def test_login_check_data_package_menu_button(index_page, main_page):
    index_page.login_flow()
    main_page.click_on_logo()
    main_page.click_on_data_package_menu()
    main_page.check_in_data_package_menu()

#re