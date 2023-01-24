import time

import pytest

@pytest.mark.ui
def test_create_200m_data_package(index_page, main_page, create_project_page, create_data_package_page):
    index_page.login_flow()
    main_page.click_on_data_package_menu()
    create_data_package_page.click_create_data_package()
    create_data_package_page.input_data_package_name()
    create_data_package_page.click_add_new_data_type()
    create_project_page.click_layer_thikness()
    create_data_package_page.click_layer_thickness_drop_down()
    create_data_package_page.click_create_new_interface_button()
    create_data_package_page.click_on_interface_drop_down_asphalt()
    create_data_package_page.click_asphalt_button_drop_dawn()
    create_data_package_page.click_to_upload_new_file_to_this_interface_asphalt_200m()
    time.sleep(10)