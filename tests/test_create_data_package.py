import time

import pytest

@pytest.mark.ui
@pytest.mark.regression
def test_create_200m_data_package(index_page, main_page, create_project_page, create_data_package_page):
    index_page.login_flow()
    main_page.click_on_data_package_menu()
    create_data_package_page.click_create_data_package()
    create_data_package_page.input_data_package_name()
    create_data_package_page.click_to_upload_new_file_to_this_interface_asphalt_200m()
    time.sleep(10)