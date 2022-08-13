import pytest

from pages.login_page import LoginPage
from tests.base_test import BaseTest
from data.locators.credentials import LoginCredentials

from selenium.webdriver.support.ui import WebDriverWait
 

class TestLogin(BaseTest):

    @pytest.fixture
    def load_pages(self):
        """"
        Loads the login page - https://hudl.com/login
        
        """
        self.page = LoginPage(self.driver, self.wait)
        self.page.go_to_login_page()

    def test_elements_on_page_are_visible(self, load_pages):
        """"
        Verifies all elements on the login page are visible
        
        """
        self.page.elements_are_visible_on_page()

    def test_succesful_login(self, load_pages):
        """"
        Tests and verifies succesful login

        """
        self.page.elements_are_visible_on_page()
        email_input = LoginCredentials.email
        password_input = LoginCredentials.password
        self.page.fill_login_form(email_input, password_input)
        self.page.login_success()

    
    def test_failed_login(self, load_pages):
        """"
        Tests and verifies failed login
        
        """
        email_input = "dummyemail@dummy.com"
        password_input = "password"
        self.page.fill_login_form(email_input, password_input)
        self.page.login_fail()
    

