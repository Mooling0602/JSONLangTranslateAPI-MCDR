<a id="jtl_api"></a>

# jtl\_api

<a id="jtl_api.parseKey"></a>

#### 导入方式：
```python
PLUGIN_METADATA = {
    'dependencies': {
        'mcdreforged': '>=2.1.0',
        'jtl_api': '>=0.1.0'
    }
}

import jtl_api
```

## parseKey

```python
def parseKey(lang, content, fileEncoding='utf-8'):
```

在指定的语言文件中使用给定的（文本）内容查找其（翻译）键名称。

**参数**:

- `file_path`: 语言文件的路径。
- `content`: 用于查找的（文本）内容。
- `fileEncoding`: 文件的编码格式，默认为`utf-8`。

**返回**:

查找到的（翻译）键名称, 没有找到则为`None`。

<a id="jtl_api.parseValue"></a>

## parseValue

```python
def parseValue(lang, key, fileEncoding='utf-8'):
```

根据给定的键从指定的语言文件中检索（翻译）值。

**参数**:

- `file_path`: 语言文件的路径。
- `key`: 用于查找的（翻译）键名称。
- `fileEncoding`: 文件的编码格式，默认为`utf-8`。

**返回**:

查找到的（翻译）值，没有找到则为`None`。

<a id="jtl_api.parseContent"></a>

## parseContent

```python
def parseContent(text):
```

【可选】通过删除（英文符）方括号来处理原始内容。

**参数**:

- `text`: （用于处理的）原始文本。

**返回**:

处理后的文本。