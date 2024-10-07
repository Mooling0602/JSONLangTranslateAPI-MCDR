import json
import re

from mcdreforged.api.all import *

def on_load(server: PluginServerInterface, old):
    server.logger.info("Loaded Game lang translate API.")
    server.logger.info("Mainly for VanillaGameEvents, but may be suitable to pack to pypi, if you're interested you can do it!")

def parseKey(lang, content, fileEncoding='utf-8'):
    """
    Find the key name for the given content in the specified language file.

    :param file_path: The path to the language file.
    :param content: The content to search for.
    :param fileEncoding: The encoding format of the file, default is 'utf-8'.
    :return: The found key name, or None if not found.
    """
    try:
        with open(lang, 'r', encoding=fileEncoding) as file:
            data = json.load(file)

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

        return search_dict(data)

    except FileNotFoundError:
        print(f"File not exists: {lang}")
        return None
    except json.JSONDecodeError:
        print(f"Can't parse json file: {lang}")
        return None

def parseValue(lang, key, fileEncoding='utf-8'):
    """
    Retrieve the value from the specified language file based on the given key.

    :param file_path: The path to the language file.
    :param key: The key name to search for.
    :param fileEncoding: The encoding format of the file, default is 'utf-8'.
    :return: The found value, or None if not found.
    """
    try:
        with open(lang, 'r', encoding=fileEncoding) as file:
            data = json.load(file)
            value = data.get(key, None)
        return value
    except FileNotFoundError:
        print(f"File not exists: {lang}")
        return None
    except json.JSONDecodeError:
        print(f"Can't parse json file: {lang}")
        return None

# Optional.
def parseContent(text):
    """
    Process the raw content by removing square brackets.

    :param text: The raw text.
    :return: The processed text.
    """
    return re.sub(r'\[|\]', '', text)
