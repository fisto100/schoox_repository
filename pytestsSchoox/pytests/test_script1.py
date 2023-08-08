"""

Login with user
Go to https://qatest.schoox.com/training
Click from Categories the QA Category
Validate that the list contains only the following items
QA Course
BA Course
Μάθημα για τους Devs
Μάθημα για Automation

"""
import pytest
from utilities.base_class import BaseClass
from page_objects.home_page import HomePage
from test_data.login_page_data import LoginPageData


class TestQACourses(BaseClass):

    def test_qa_courses(self, data):

        log = self.get_logger()
        log.info("Logging in ...")
        self.login(data["email"], data["password"])

        log.info("Checking if Login was successful ...")
        url = self.driver.current_url
        assert url == "http://qatest.schoox.com/", "Incorrect Credentials!!!, Couldn't Login"

        homepage = HomePage(self.driver)
        trainingpage = homepage.training_tab()

        trainingpage.qa_category_filter().click()
        courses = trainingpage.course_titles()

        expected_list_of_courses = ["QA Course", "BA Course", "Μάθημα για τους Devs", "Μάθημα για Automation"]

        log.info("Creating a list of lessons ...")
        list_of_courses = list()
        for course in courses:
            course_title = course.text
            list_of_courses.append(course_title.lower())

        log.info("Checking number of lessons ...")
        assert len(courses) == 4

        log.info("Validating the results ...")
        for element in list_of_courses:
            assert element in self.all_lower(expected_list_of_courses), element + " is not in expected list of courses"

        log.info("Logging out ...")
        trainingpage.log_out().click()

    @pytest.fixture(params=LoginPageData.credentials_list)
    def data(self, request):
        return request.param
