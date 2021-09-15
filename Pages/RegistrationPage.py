from Pages.BasePage import BasePage
from Utilities import configReader


class RegistrationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def fillform(self, name, phone, email, country, city, username, password):
        self.type("name_CSS", name)
        self.type("phone_CSS", str(phone))
        self.type("email_CSS", email)
        self.select("country_CSS", country)
        self.type("city_CSS", city)
        self.type("username_CSS", username)
        self.type("password_CSS", password)
        self.click("submit_CSS")
