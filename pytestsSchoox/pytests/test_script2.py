"""
Login with user
Go to https://qatest.schoox.com/6/steps
Enroll to the course
Complete all the steps
Validate that the progress is 100%
"""


from page_objects.home_page import HomePage
from utilities.base_class import BaseClass


class TestCourseProgress(BaseClass):

    def test_course_progress(self):

        log = self.get_logger()
        log.info("Logging in ...")
        self.login("admin@schoox.com", "123456")

        log.info("Checking if Login was successful ...")
        url = self.driver.current_url
        assert url == "http://qatest.schoox.com/", "Incorrect Credentials!!!, Couldn't Login"

        log.info("Enrolling ...")
        homepage = HomePage(self.driver)
        trainingpage = homepage.training_tab()

        automationlessonspage = trainingpage.automation_course()

        automationlessonspage.enroll_button().click()

        log.info("Finding out the number of the lessons ...")
        number_of_lessons = len(automationlessonspage.all_lessons())
        log.info("Number of Lessons: " + str(number_of_lessons))
        log.info("Completing Lessons ...")
        for index, element in enumerate(range(number_of_lessons)):
            automationlessonspage.completion_button().click()
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            alert.accept()
            log.info("Alert: " + alert_text + " - Clicked OK - " + str(index+1) + " of " + str(number_of_lessons))
        log.info("Checking progress ...")
        progress_output = automationlessonspage.course_progress().text
        log.info(progress_output)

        course_progress_int = int(progress_output.split(".")[0].split(" ")[2])
        print(str(course_progress_int))
        log.info("Validating it is 100%")
        assert course_progress_int == 100, "Expected 100% course progress, but it's " + str(course_progress_int)

        log.info("Logging out ...")
        automationlessonspage.log_out().click()