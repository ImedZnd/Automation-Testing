import pytest

from Pages.RegistrationPage import RegistrationPage
from Testcases.BaseTest import BaseTest
from Utilities import dataProvider
import logging
from Utilities.LogUtil import Logger

log = Logger(__name__,logging.INFO)

class Test_SignUpTest(BaseTest):

    @pytest.mark.parametrize("name, phone, email, country, city, username, password",
                             dataProvider.get_data("LoginTest"))
    def test_doSignUp(self, name, phone, email, country, city, username, password):
        log.logger.info("Test Do Sign Up Started ")
        regPage = RegistrationPage(self.driver)
        regPage.fillform(name, phone, email, country, city, username, password)
        log.logger.info("Test Do Sign Up Finiched ")
