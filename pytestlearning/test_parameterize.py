import pytest


def get_data():
    return [
        ("username1@gmail.com", "password1"),
        ("username2@gmail.com", "password2"),
        ("username3@gmail.com", "password3")
    ]


@pytest.mark.parametrize("username,password", get_data())
def test_do_login(username, password):
    print(username + "-----" + password)

