from selenium.webdriver.common.by import By


class LoginPageLocators:
    email_address = (By.XPATH, "//input[@id='email']")
    password = (By.XPATH, "//input[@id='password']")
    login_button = (By.CSS_SELECTOR, "#logIn")
    remember_me_radio_box = (By.XPATH, "//label[@for='uniId_2']//*[name()='svg']//*[name()='rect'][1]")
    remember_me_link = (By.XPATH, "//label[@for='uniId_2']")
    help_link = (By.XPATH, "//a[@class='uni-link uni-link--default']")
    login_with_organization_link = (By.XPATH, "//button[@type='button']")
    back_button = (By.XPATH, "//a[@class='styles_backIconContainer_MhkioW9m8rx70X7CIGuws']//*[name()='svg']")
    sign_up_link = (By.XPATH, "//a[@class='uni-link uni-link--default styles_signUpLink_1CPc8TbK9yDyBdJiSpUOZV']")
    home_icon = (By.XPATH, "//a[@class='uni-link uni-link--wrapper styles_hudlLogoContainer_1L8Lig-sH69T84pB_fXSlv styles_fadeInUpFast_13tTIPxY77Mkw_Ud-lEwlP']")
    error_message = (By.XPATH, ".uni-text")
