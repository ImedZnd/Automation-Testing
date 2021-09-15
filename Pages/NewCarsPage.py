from Pages.BasePage import BasePage


class NewCarsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def select_kia(self):
        self.click("kia_CSS")

    def select_toyota(self):
        self.click("toyota_CSS")

    def select_bmw(self):
        self.click("bmw_CSS")

    def select_honda(self):
        self.click("honda_CSS")


