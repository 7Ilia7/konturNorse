import pytest

@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.regression
def test_create_200m_project(index_page, main_page, create_project_page):
    index_page.login_flow()
    main_page.click_on_btn_start_new_project()
    create_project_page.input_project_name()
    create_project_page.choose_data_package()
    create_project_page.btn_next()
    create_project_page.btn_start_build_project()
    create_project_page.click_layer_thikness()
    create_project_page.input_layer_name()
    create_project_page.click_top_layer_dropdown()
    create_project_page.click_asphalt_bottom()
    create_project_page.click_bottom_layer_dropdown()
    create_project_page.click_bottom_bottom_layer()
    create_project_page.add_selected_tracker()
    create_project_page.create_project_btn()
    create_project_page.check_200m_project_was_created()
    create_project_page.delete_first_project_in_list_btn_delete()
    create_project_page.delete_project_btn_yes()
    main_page.check_that_we_not_have_any_project()

@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.regression
def test_create_14km_project(index_page, main_page, create_project_page):
    index_page.login_flow()
    main_page.click_on_btn_start_new_project()
    create_project_page.input_project_name_14km_all_tracker()
    create_project_page.choose_data_package_14km()
    create_project_page.btn_next()
    create_project_page.btn_start_build_project()
    create_project_page.click_layer_thikness()
    create_project_page.input_layer_name()
    create_project_page.click_top_layer_dropdown()
    create_project_page.click_asphalt_bottom()
    create_project_page.click_bottom_layer_dropdown()
    create_project_page.click_bottom_bottom_layer()
    create_project_page.add_selected_tracker()
# начинаем создавать деламинейшин слой
    create_project_page.add_more_tracker_btn()
    create_project_page.click_delam_layer()
    create_project_page.input_name_delam_layer_field()
    create_project_page.choose_asphalt_layer()
    create_project_page.add_selected_tracker_delam()
# Начинаем создавать крек слой
    create_project_page.add_more_tracker_btn()
    create_project_page.click_add_crack_layer()
    create_project_page.input_name_crack_layer()
    create_project_page.check_box_asphalt_layer()
    create_project_page.check_box_base_bottom_crack()
    create_project_page.add_selected_tracker()
    create_project_page.create_project_btn()
#  Проверяем наличее созданного проекта и удаляем его.
    create_project_page.check_14km_project_was_created()
    create_project_page.delete_first_project_in_list_btn_delete()
    create_project_page.delete_project_btn_yes()
    main_page.check_that_we_not_have_any_project()