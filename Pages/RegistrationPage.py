from selenium.webdriver.support.select import Select

from Pages.BasePage import BasePage
from Utilities import configReader


class RegistrationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def fillform(self, name, phone, email, country, city, username, password):
        self.type("name_CSS", name)
        self.type("phone_CSS", phone)
        self.type("email_CSS", email)
        dropdown = self.driver.find_element_by_css(configReader.read_config("locators", ""))
        select = Select(dropdown)
        select.select_by_visible_text(country)
        self.type("", city)
        self.type("username_CSS", username)
        self.type("password_CSS", password)
        self.click("submit_CSS")
