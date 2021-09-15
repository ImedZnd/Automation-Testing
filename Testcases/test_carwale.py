import time

import pytest

from Pages.HomePage import HomePage
from Pages.NewCarsPage import NewCarsPage
from Pages.RegistrationPage import RegistrationPage
from Testcases.BaseTest import BaseTest
from Utilities import dataProvider
import logging
from Utilities.LogUtil import Logger

log = Logger(__name__,logging.INFO)

class Test_Carwale(BaseTest):

    def test_goto_new_car(self):
        log.logger.info("go to new car ")
        home = HomePage(self.driver)
        home.goto_new_cars()
        time.sleep(3)

    @pytest.mark.parametrize("carBrand, carTitle",dataProvider.get_data("NewCarsTest"))
    def test_select_cars(self, carBrand, carTitle):
        log.logger.info("select car ")
        home = HomePage(self.driver)
        if carBrand == "BMW":
            home.goto_new_cars().select_bmw()
        elif carBrand == "Kia":
            home.goto_new_cars().select_kia()
        elif carBrand == "Honda":
            home.goto_new_cars().select_honda()
        elif carBrand == "Toyota":
            home.goto_new_cars().select_toyota()

        time.sleep(3)