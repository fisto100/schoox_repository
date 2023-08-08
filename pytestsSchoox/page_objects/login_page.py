from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    email_locator = (By.CSS_SELECTOR, "div input[type='email']")
    password_locator = (By.CSS_SELECTOR, "div input[type='password']")
    submit_button_locator = (By.CSS_SELECTOR, "button[type='submit']")

    def email_input(self):
        return self.driver.find_element(*LoginPage.email_locator)

    def password_input(self):
        return self.driver.find_element(*LoginPage.password_locator)

    def submit_button(self):
        return self.driver.find_element(*LoginPage.submit_button_locator)
