from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest


def setup_function():
    global driver
    driver = webdriver.Chrome(executable_path=ChromeDriverManager.install())
    driver.get("https://facebook.com")
    driver.maximize_window()


def teardown_function():
    driver.quit()


def get_data():
    return [
        ("username1@gmail.com", "password1"),
        ("username2@gmail.com", "password2"),
        ("username3@gmail.com", "password3")
    ]


@pytest.mark.parametrize("username,password", get_data())
def test_do_login(username, password):
    print(username + "-----" + password)
