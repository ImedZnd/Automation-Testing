from Pages.BasePage import BasePage
from Pages.NewCarsPage import NewCarsPage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def goto_new_cars(self):
        self.moveto("newCars_XPATH")
        self.click("findNewCar_XPATH")

        return NewCarsPage(self.driver)

    def goto_compare_cars(self):
        pass

    def goto_used_cars(self):
        pass


