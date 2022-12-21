import time


def test_first(index_page, main_page):
    index_page.login_flow()
    main_page.click_on_data_package_menu()
    time.sleep(2)
    main_page.click_on_logo()
    time.sleep(2)
    main_page.click_on_user_management()
    time.sleep(2)
    main_page.click_on_projects_btn_menu()
    time.sleep(2)
    main_page.click_om_tile_projects_display()
    time.sleep(2)
    main_page.click_om_list_projects_display()
    time.sleep(2)
    main_page.click_on_profile_btn()

