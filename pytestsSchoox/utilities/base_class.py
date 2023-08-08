import inspect
import pytest
import logging
from page_objects.login_page import LoginPage


@pytest.mark.usefixtures("setup")
class BaseClass:

    def login(self, mail, psw):
        loginpage = LoginPage(self.driver)
        loginpage.email_input().send_keys(mail)
        loginpage.password_input().send_keys(psw)
        loginpage.submit_button().click()

    @staticmethod
    def all_lower(my_list):
        return [x.lower() for x in my_list]

    @staticmethod
    def get_logger():
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        file_handler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.setLevel(logging.INFO)
        return logger

