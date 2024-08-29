# 用法
> 目前仅适用于MCDR插件
>
> 提供的代码仅供参考，你可以自行根据实际情况进行修改
> 
## 当前限制
- 准备的语言文件最好是原文和译文一一对应，否则可能无法正确翻译
- 你需要自行处理因没有满足上一条而产生的各种报错
- 有些文本会匹配到多条翻译键导致翻译出多个结果，你可能需要手动处理因此产生的错误

## [代码参考](https://github.com/Mooling0602/AnotherTranslateAPI-MCDR/blob/0.0.1/example/example.py)
1. 导入该API
- `from atl_api import parseKey, parseValue, parseContent`
2. 准备至少两个要用于翻译的游戏语言文件，分为`raw_lang`和`translated_lang`，并在代码内或通过插件配置设置其路径
3. 获取你要翻译的内容，保证其为单行的字符串，假设其为`raw_content`
4. 【可选】对要翻译的内容（原文）进行预处理，避免解析错误，使用`content = parseContent(raw_content)`
5. 获取译文，假设译文为`tr_content`，则`tr_content = parseValue(translated_lang, parseKey(raw_lang, content))`；或分为两步，先匹配原文对应的翻译键名称`key = parseKey(raw_lang, content)`，再匹配到译文内容`tr_content = parseValue(translated_lang, key)`


