from pages.base_page import BasePage

from data.locators.home_page_locators import HomePageLocators
from data.locators.login_page_locators import LoginPageLocators

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver

import requests
import time


class LoginPage(BasePage):

    def __init__(self, driver, wait):
        self.url = "https://hudl.com/login/"
        self.LoginLocator = LoginPageLocators
        super().__init__(driver, wait)

    def go_to_login_page(self):
        """
        Navigates user to the login page
        """
        self.go_to_page(self.url)

    def elements_are_visible_on_page(self):
        """
        Verifies elements exist on page
        """
        self.go_to_page(self.url)

        self.driver.find_element(*self.LoginLocator.email_address).is_displayed
        self.driver.find_element(*self.LoginLocator.password).is_displayed
        self.driver.find_element(*self.LoginLocator.remember_me_radio_box).is_displayed
        self.driver.find_element(*self.LoginLocator.remember_me_link).is_displayed
        self.driver.find_element(*self.LoginLocator.help_link).is_displayed
        self.driver.find_element(*self.LoginLocator.login_with_organization_link).is_displayed
        self.driver.find_element(*self.LoginLocator.back_button).is_displayed
        self.driver.find_element(*self.LoginLocator.sign_up_link).is_displayed
        self.driver.find_element(*self.LoginLocator.home_icon).is_displayed
        self.driver.find_element(*self.LoginLocator.login_button).is_displayed

        self.driver.save_screenshot("results/elements_are_visible_on_page.png")


    def fill_login_form(self, email_input, password_input):
        """
        Fills login form with credentials sent in as arguments

        """
        self.driver.find_element(*self.LoginLocator.email_address).send_keys(email_input)
        self.driver.find_element(*self.LoginLocator.password).send_keys(password_input)

    def remember_me(self):
        """"
        selects remember_me on login
        """
        self.driver.find_element(*self.LoginLocator.remember_me_radio_box).click
        self.driver.save_screenshot("results/remember_me_selected.png")

    def login_success(self):
        """
        Verifies login is successful by locating an element on the page and attempting to navigate the page
        """
        self.driver.find_element(*self.LoginLocator.login_button).click()
        time.sleep(4)
        elem = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(HomePageLocators.home_link)
            )        

        self.driver.save_screenshot("results/login_success_hudl_home.png")
    
    def login_fail(self):
        """
        Verfies failure message for a bad login attempt

        """
        self.driver.find_element(*self.LoginLocator.login_button).click()
        time.sleep(4)
        error_message = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.uni-text'))
            )  
        self.driver.save_screenshot("results/login_fail_message.png")
      



    
