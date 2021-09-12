def setup_module(module):  # test fixture lunch before every test module
    print('creating DB connection')


def teardown_module(module):  # test fixture lunch at the end of every test module
    print('closing DB connection')


def setup_function(function):  # test fixture lunch before every test function
    print('Lunching browser')


def teardown_function(function):  # test fixture lunch at the end of every test function
    print('closing browser')


def test_do_login():
    print('executing login test')


def test_do_reg():
    print('executing reg test')
