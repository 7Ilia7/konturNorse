import time


def test_first(index_page, main_page):
    index_page.input_correct_user_name()
    index_page.input_correct_password()
    index_page.click_login()
    main_page.click_on_data_package_menu()
    main_page.click_on_logo()
    main_page.click_on_user_management()
    main_page.click_on_projects_btn_menu()
    main_page.click_om_tile_projects_display()
    main_page.click_om_list_projects_display()
    main_page.click_on_profile_btn()
