from selenium.webdriver.common.by import By

class HomePageLocators:
    home_link = (By.XPATH, "//span[normalize-space()='Home']")
    current_user = (By.XPATH, "//div[@class='uni-avatar__content-container']")
