import json
import re

from mcdreforged.api.all import *

def on_load(server: PluginServerInterface, old):
    server.logger.info("Loaded AnotherTranslateAPI.")

# 匹配翻译键名
def parseKey(lang, content, fileEncoding='utf-8'):
    with open(lang, 'r', encoding=fileEncoding) as file:
        data = json.load(file)
    for key, value in data.items():
        if value == content:
            return key
    return None

# 匹配翻译值
def parseValue(lang, key, fileEncoding='utf-8'):
    with open(lang, 'r', encoding=fileEncoding) as file:
        data = json.load(file)
        value = data.get(key, None)
    return value

# （可选）处理原始内容
def parseContent(text):
    return re.sub(r'\[|\]', '', text)
