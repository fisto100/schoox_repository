from selenium.webdriver.common.by import By
from page_objects.automation_lessons_page import AutomationLessonsPage


class TrainingPage:

    def __init__(self, driver):
        self.driver = driver

    qa_category = (By.CSS_SELECTOR, "div[class='category_item']:nth-child(3)")
    courses = (By.CSS_SELECTOR, ".course_title")
    automation = (By.LINK_TEXT, "Μάθημα για automation")
    logout = (By.XPATH, "//div[5]")

    def qa_category_filter(self):
        return self.driver.find_element(*TrainingPage.qa_category)

    def course_titles(self):
        return self.driver.find_elements(*TrainingPage.courses)

    def automation_course(self):
        self.driver.find_element(*TrainingPage.automation).click()
        automationlessonspage = AutomationLessonsPage(self.driver)
        return automationlessonspage

    def log_out(self):
        return self.driver.find_element(*AutomationLessonsPage.logout)
