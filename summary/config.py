import os
import configparser
from .print_utils import print_colored, input_colored

CONFIG_FILE = os.path.join(os.path.dirname(__file__), "config.ini")


def is_valid_api_key(api_key):
    if not api_key or api_key.isspace():
        return False
    return True


def get_config():
    config = configparser.ConfigParser()
    if os.path.exists(CONFIG_FILE):
        config.read(CONFIG_FILE)
        return config
    else:
        return None


def save_config(config):
    with open(CONFIG_FILE, "w") as configfile:
        config.write(configfile)


def get_api_key():
    config = get_config()
    if config is None:
        config = configparser.ConfigParser()
        config.add_section("OpenAI")

        while True:
            api_key = input_colored("Please enter your OpenAI API Key: ", level="info")
            if is_valid_api_key(api_key):
                config.set("OpenAI", "api_key", api_key)
                save_config(config)
                break
            else:
                print_colored("Invalid API key. Please try again.", level="error")

        return api_key
    else:
        return config.get("OpenAI", "api_key", fallback=None)
