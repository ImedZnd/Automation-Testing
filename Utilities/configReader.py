from configparser import ConfigParser

# config = ConfigParser()
# config.read('config.ini')
#
# print(config.get("locator", "username"))
# print(config.get("basic info", "testsiteurl"))


def read_config(section, key):
    config = ConfigParser()
    config.read('config.ini')
    return config.get(section, key)

print(read_config("basic info", "testsiteurl"))
