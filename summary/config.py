import os
import configparser

CONFIG_FILE = os.path.join(os.path.dirname(__file__), "config.ini")


def is_valid_api_key(api_key):
    if api_key is None:
        return False
    return len(api_key) > 10 and api_key.startswith("sk-")


def get_config():
    config = configparser.ConfigParser()
    if os.path.exists(CONFIG_FILE):
        config.read(CONFIG_FILE)
        return config
    else:
        return None


def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        config.write(f)


def get_api_key():
    config = get_config()
    if config is None:
        config = configparser.ConfigParser()
        config.add_section("OpenAI")

        while True:
            api_key = input("Please enter your OpenAI API Key: ")
            if is_valid_api_key(api_key):
                config.set("OpenAI", "api_key", api_key)
                save_config(config)
                break
            else:
                print("Invalid API key. Please try again.")

        return api_key
    else:
        return config.get("OpenAI", "api_key", fallback=None)
