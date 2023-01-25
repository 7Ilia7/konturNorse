from selenium.webdriver.common.by import By

class Locators:
    USER_NAME_FIELD = (By.CSS_SELECTOR, '.MuiOutlinedInput-input.MuiInputBase-input.css-1sxenmq')
    PASSWORD_FIELD = (By.ID, ':r1:')
    LOGIN_BTN = (By.CSS_SELECTOR, '.MuiBox-root.css-1yuhhex button')
    ACTUAL_TEXT = (By.CSS_SELECTOR, '.MuiTypography-root.MuiTypography-h5.css-1spu3xu')
    ACTUAL_TEXT_WRONG_DATA = (By.CSS_SELECTOR, '.MuiAlert-message.css-1w0ym84')
    ACTUAL_TEXT_WHEN_NO_EMAIL = (By.ID, ':r0:-label')
    ACTUAL_TEXT_WHEN_NO_PASSWORD = (By.CSS_SELECTOR, '.MuiTypography-root.MuiTypography-body1.css-qxa0uy')
    FORGOT_PASSWORD = (By.CSS_SELECTOR, '.MuiTypography-root.MuiTypography-inherit.MuiLink-root.MuiLink-underlineAlways.sign-in__forgot-password-link.css-1aeq63l')
    FORGOT_PASSWORD_EMAIL_INPUT = (By.CSS_SELECTOR, '.MuiOutlinedInput-input.MuiInputBase-input.css-1sxenmq')
    ACTUAL_TEXT_APPLY_EMAIL_FOR_FORGOT_PASS = (By.CSS_SELECTOR, '.MuiAlert-message.css-1w0ym84')
    RESTORE_PASSWORD_BUTTON = (By.CSS_SELECTOR, '.MuiButton-root.MuiButton-contained.MuiButton-containedPrimary.MuiButton-sizeMedium.MuiButton-containedSizeMedium.MuiButtonBase-root.css-1yawhyg')
    SIGN_IN_BTN_ON_FG_PAGE = (By.CSS_SELECTOR, '.MuiTypography-root.MuiTypography-inherit.MuiLink-root.MuiLink-underlineAlways.css-1geud7x')
    SIGN_IN_TXT_ON_MAIN = (By.CSS_SELECTOR, '.MuiTypography-root.MuiTypography-h5.css-178m04z')

class MainPageLocators:
    LOGO_BTN = (By.CSS_SELECTOR, '.logo')
    PROJECTS_BTN = (By.CSS_SELECTOR, '.MuiBox-root.css-2sya8s div:nth-child(1)')
    DATA_PACKAGE_BTN = (By.CSS_SELECTOR, '.MuiBox-root.css-2sya8s div:nth-child(2)')
    DATA_PACKAGE_TXT = (By.CSS_SELECTOR, '.MuiTypography-root.MuiTypography-h5.css-mw8q1s')
    USER_MANAGEMENT_BTN = (By.CSS_SELECTOR, '.MuiBox-root.css-2sya8s div:nth-child(3)')
    PROFILE_BTN = (By.CSS_SELECTOR, '.MuiAvatar-root.MuiAvatar-circular.MuiAvatar-colorDefault.css-xe3wy')
    PROJECTS_BTN_LIST = (By.CSS_SELECTOR, '.MuiBox-root.css-70qvj9 button:nth-child(3)')
    PROJECTS_BTN_TILE = (By.CSS_SELECTOR, '.MuiBox-root.css-70qvj9 button:nth-child(2)')
    START_NEW_PROJECTS_BTN = (By.CSS_SELECTOR, '.MuiBox-root.css-70qvj9 button:nth-child(4)')
    FIND_200M_PROJECT = (By.XPATH, '//p[contains(text(),"200mTest")]')
    FIND_14KM_PROJECT = (By.XPATH, '//p[contains(text(),"14km_all_tracker")]')
    DELETE_FIRST_PROJECT_IN_LIST = (By.CSS_SELECTOR, '.MuiButtonBase-root.MuiIconButton-root.MuiIconButton-sizeMedium.css-1yxmbwk')
    DELETE_YES = (By.CSS_SELECTOR, '.MuiBox-root.css-1l4w6pd button:nth-child(1)')
    DELETE_NO = (By.CSS_SELECTOR, '.MuiBox-root.css-1l4w6pd button:nth-child(2)')
    TEXT_WHEN_WE_HAVE_ANY_PROJECT = (By.CSS_SELECTOR, '.MuiTypography-root.MuiTypography-body1.MuiTypography-alignCenter.css-ustd3q')
    PROCESSING = (By.XPATH, '//p[contains(text(),"processing")]')


class CreateProjectsLocator:
    PROJECT_NAME_FIELD = (By.CSS_SELECTOR, '.MuiInputBase-input.MuiOutlinedInput-input.css-1sxenmq')

    UNIT_SYSTEM_MENU_CLICK = (By.CSS_SELECTOR, '.MuiBox-root.css-2imjyh div:nth-child(3) div:nth-child(2)')
    METRIC = (By.CSS_SELECTOR, '.MuiList-root.MuiList-padding.MuiMenu-list.css-r8u8y9 li:nth-child(1)')
    IMPERIAL = (By.CSS_SELECTOR, '.MuiList-root.MuiList-padding.MuiMenu-list.css-r8u8y9 li:nth-child(2)')

    COORDINATE_SYSTEM_MENU = (By.CSS_SELECTOR, '.MuiSelect-select.MuiSelect-outlined.MuiInputBase-input.MuiOutlinedInput-input.css-2088s5')
    COORDINATE_4226 = (By.CSS_SELECTOR, '.MuiList-root.MuiList-padding.MuiMenu-list.css-r8u8y9 li:nth-child(1)')
    COORDINATE_3857 = (By.CSS_SELECTOR, '.MuiList-root.MuiList-padding.MuiMenu-list.css-r8u8y9 li:nth-child(2)')

    CHOOSE_DATA_PACKAGE_200M = (By.XPATH, '//div[contains(text(),"200mTestQa")]')
    CHOOSE_DATA_PACKAGE_14KM = (By.XPATH, '//div[contains(text(),"14kmAllTracker")]')

    BTN_NEXT = (By.CSS_SELECTOR, '.MuiBox-root.css-1oevkxy button:nth-child(2)')
    BTN_START_BUILDING_PROJ = (By.CSS_SELECTOR, '.MuiBox-root.css-ndh2dq button')
    # Thikness layer
    LAYER_THIKNESS = (By.CSS_SELECTOR, '.MuiCardContent-root.css-5y4tke')
    INPUT_LAYER_NAME = (By.CSS_SELECTOR, '.MuiInputBase-input.MuiOutlinedInput-input.css-1sxenmq')

    BTN_TOP = (By.CSS_SELECTOR, '.MuiSelect-select.MuiSelect-outlined.MuiInputBase-input.MuiOutlinedInput-input.MuiInputBase-inputAdornedStart.css-pgaui2')
    ASPHALT_BOTTOM = (By.CSS_SELECTOR, '.MuiList-root.MuiList-padding.MuiMenu-list.css-r8u8y9 li:nth-child(2)')

    BTN_BOTTOM = (By.CSS_SELECTOR, '.css-1s2p0j8 div:nth-child(3) div:nth-child(2)')
    BASE_BOTTOM = (By.CSS_SELECTOR, '.MuiList-root.MuiList-padding.MuiMenu-list.css-r8u8y9 li:nth-child(2)')

    ADD_SELECTED_TRACKER_BTN = (By.CSS_SELECTOR, '.MuiBox-root.css-1h9zagw button:nth-child(2)')

    CREATE_PROJECT_BTN = (By.CSS_SELECTOR, '.MuiBox-root.css-1oevkxy button:nth-child(2)')

    ADD_MORE_TRACKER_BTN = (By.CSS_SELECTOR, '.MuiButtonBase-root.MuiButton-root.MuiButton-contained.MuiButton-containedPrimary.MuiButton-sizeMedium.MuiButton-containedSizeMedium.css-o0z51j')

#     Delam Menu
    DELAM = (By.CSS_SELECTOR, '.MuiBox-root.css-abw72h div:nth-child(2)')
    NAME_INPUT_FIELD_DELAM_OR_CRACK = (By.CSS_SELECTOR, '.MuiInputBase-input.MuiOutlinedInput-input.css-1sxenmq')
    CHECK_ASPH_BASE_BOTTOM = (By.XPATH, '//span[contains(text(),"Base bottom")]')
    CHECK_SURFACE_ASPH_BOTTOM = (By.XPATH, '//span[contains(text(),"Surface")]')
    ADD_SELECTED_TRACKER_BTN_DELAM = (By.CSS_SELECTOR, '.MuiBox-root.css-1h9zagw button:nth-child(2)')

#     Crack Menu
    CRACK = (By.CSS_SELECTOR, '.MuiGrid-root.MuiGrid-container.MuiGrid-spacing-xs-4.css-17xlo9l  div:nth-child(3)')
    CHECK_BASE_BOTTOM_CRACK = (By.XPATH, '//span[contains(text(),"Base bottom")]')
    CHECK_ASPHALT_BOTTOM_CRACK = (By.XPATH, '//span[contains(text(),"Asphalt bottom")]')
    CHECK_SURFACE_CRACK = (By.XPATH, '//span[contains(text(),"Surface")]')

class DataPackagePageLocators:
    CREATE_DATA_PACKAGE_BUTTON = (By.XPATH, '//button[contains(text(),"Create new data package")]')
    NAME_DATA_PACKAGE = (By.CSS_SELECTOR, '.MuiInputBase-input.MuiOutlinedInput-input.css-1sxenmq')
    ADD_NEW_DATA_TYPE = (By.XPATH, '//button[contains(text(),"Add new data type")]')
    UPLOAD_DATA_PACKAGE_FILE = (By.TAG_NAME, '[for=":rf:"] span')

