from Utilities import configReader


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        if str(locator).endswith("_CSS"):
            self.driver.find_element_by_css_selector(configReader.read_config("locators", locator)).click()
        elif str(locator).endswith("_XPATH"):
            self.driver.find_element_by_xpath(configReader.read_config("locators", locator)).click()
        elif str(locator).endswith("_ID"):
            self.driver.find_element_by_id(configReader.read_config("locators", locator)).click()

    def click(self, locator, value):
        if str(locator).endswith("_CSS"):
            self.driver.find_element_by_css_selector(configReader.read_config("locators", locator)).send_keys(value)
        elif str(locator).endswith("_XPATH"):
            self.driver.find_element_by_xpath(configReader.read_config("locators", locator)).send_keys(value)
        elif str(locator).endswith("_ID"):
            self.driver.find_element_by_id(configReader.read_config("locators", locator)).send_keys(value)
