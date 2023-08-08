from selenium.webdriver.common.by import By


class AutomationLessonsPage:

    def __init__(self, driver):
        self.driver = driver

    enroll = (By.CSS_SELECTOR, ".enroll")
    lessons = (By.CSS_SELECTOR, ".course_main_row")
    buttons = (By.CSS_SELECTOR, "div[class='course_steps_right'] div[class='dot']")
    progress = (By.CSS_SELECTOR, ".top_course_progress")
    logout = (By.XPATH, "//div[5]")

    def enroll_button(self):
        return self.driver.find_element(*AutomationLessonsPage.enroll)

    def all_lessons(self):
        return self.driver.find_elements(*AutomationLessonsPage.lessons)

    def completion_button(self):
        return self.driver.find_element(*AutomationLessonsPage.buttons)

    def course_progress(self):
        return self.driver.find_element(*AutomationLessonsPage.progress)

    def log_out(self):
        return self.driver.find_element(*AutomationLessonsPage.logout)
