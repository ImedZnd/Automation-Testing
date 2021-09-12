import pytest


@pytest.fixture(scope='module')
def setup():
    print('connect DB')

    yield
    print('closing connection DB')


@pytest.fixture(scope='function')
def before_after():
    print('lunching browser')

    yield
    print('closing browser')


def test_do_login(setup, before_after):
    print('executing login test')


def test_do_reg(setup, before_after):
    print('executing reg test')
