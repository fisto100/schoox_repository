from selenium.webdriver.common.by import By
from page_objects.training_page import TrainingPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    training = (By.LINK_TEXT, "Training")
    admin = (By.LINK_TEXT, "Admin")
    logout = (By.XPATH, "//div[5]")

    def training_tab(self):
        self.driver.find_element(*HomePage.training).click()
        trainingpage = TrainingPage(self.driver)
        return trainingpage

    def admin_tab(self):
        return self.driver.find_element(*HomePage.admin)

    def log_out(self):
        return self.driver.find_element(*AutomationLessonsPage.logout)
