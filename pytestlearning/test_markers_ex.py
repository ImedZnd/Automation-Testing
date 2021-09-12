import pytest


@pytest.mark.regression
def test_login():
    print('executing logging test')


@pytest.mark.functional
def test_user_reg():
    print('executing user reg test')


@pytest.mark.regression
def test_compose_email():
    print('executing compose email test')


@pytest.mark.skip
def test_skip():
    print("skipping test")
