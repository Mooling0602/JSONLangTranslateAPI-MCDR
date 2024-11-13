import json5
import re

from mcdreforged.api.all import *

def on_load(server: PluginServerInterface, prev_module):
    server.logger.info("Loaded JSON lang translate API.")
    server.logger.info("Mainly for VanillaGameEvents, but may be suitable to pack to pypi, if you're interested you can do it!")

def lang_loader(lang_path: str, encoding='utf-8'):
    """
    Load the json lang files

    :param lang_path: The path to the language file
    :param encoding: The encoding format of the file, default is 'utf-8'.
    """
    try:
        with open(lang_path, 'r', encoding=encoding) as file:
            lang = json5.load(file)
        return lang
    except FileNotFoundError:
        print(f"File not exists: {lang}")
        return None
    except ValueError:
        print(f"Can't parse json file: {lang}")
        return None

def parseKey(lang, content):
    """
    Find the key name for the given content in the specified language file.

    :param lang: The instance of `lang_loader(lang_path, encoding)`.
    :param content: The content to search for.
    :return: The found key name, or None if not found.
    """
    def search_dict(d):
        for key, value in d.items():
            if value == content:
                return key
            if isinstance(value, str) and content in value:
                return key
            if isinstance(value, dict):
                found_key = search_dict(value)
                if found_key:
                    return found_key
        return None

    return search_dict(lang)

def parseValue(lang, key):
    """
    Retrieve the value from the specified language file based on the given key.

    :param lang: The instance of `lang_loader()`.
    :param key: The key name to search for.
    :return: The found value, or None if not found.
    """
    value = lang.get(key, None)
    return value

# Optional.
def parseContent(text):
    """
    Process the raw content by removing square brackets.

    :param text: The raw text.
    :return: The processed text.
    """
    return re.sub(r'\[|\]', '', text)
