def test_create_200m_project(index_page, main_page, create_project_page):
    index_page.input_correct_user_name()
    index_page.input_correct_password()
    index_page.click_login()
    main_page.click_on_projects_btn_menu()