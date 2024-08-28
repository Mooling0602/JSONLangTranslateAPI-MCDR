# 这里是参考代码，附带详细的注释说明
# 这里的代码不会被实际引用执行，也不能直接使用
import json
import re

from mcdreforged.api.all import *
from atl_api import parseKey, parseValue, parseContent

# 原文语言文件
raw_lang = 'config/your_plugin_id/en_us.json'
# 译文语言文件
translated_lang = 'config/your_plugin_id/zh_cn.json'

# 需要使用atl_api的主函数部分
def main():
    # 需要进行翻译的原文内容
    raw_content = str
    # 对原始内容进行处理（可选）
    content = parseContent(raw_content)
    # 简化从语言文件中寻找对应的键名的方法为key方法
    key = parseKey(raw_lang, content)
    # 获取译文内容
    tr_content = parseValue(translated_lang, key)
