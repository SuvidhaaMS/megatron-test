from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage():
    def __init__(self,driver):
        self.driver = driver

    def wait_for_login_page_to_load(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(expected_conditions.visibility_of(self.driver.find_element_by_name("Login Form")))

    def get_username_textbox(self):
        try:
            element = self.driver.find_element_by_name('email')
            return element
        except:
            return None

    def get_password_textbox(self):
        try:
            return self.driver.find_element_by_name('pass')
        except:
            return None

    def get_login_button(self):
        try:
            return self.driver.find_element_by_xpath("//input[@type='submit']")
        except:
            return None

    def get_login_error_msg(self):
        try:
            return self.driver.find_element_by_xpath("//span[contains(text(), 'Password is invalid')]")
        except:
            return None