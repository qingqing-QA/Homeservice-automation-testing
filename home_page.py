from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    username_input = (By.ID, "username")
    password_input = (By.ID, "password")
    login_button = (By.ID, "loginBtn")

    def login(self, username, password):
        self.input_text(self.username_input, username)
        self.input_text(self.password_input, password)
        self.click(self.login_button)
