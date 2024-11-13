<a id="jtl_api"></a>

# jtl\_api

<a id="jtl_api.parseKey"></a>

#### Import method:
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

Find the key name for the given content in the specified language file.

**Arguments**:

- `file_path`: The path to the language file.
- `content`: The content to search for.
- `fileEncoding`: The encoding format of the file, default is 'utf-8'.

**Returns**:

The found key name, or None if not found.

<a id="jtl_api.parseValue"></a>

## parseValue

```python
def parseValue(lang, key, fileEncoding='utf-8'):
```

Retrieve the value from the specified language file based on the given key.

**Arguments**:

- `file_path`: The path to the language file.
- `key`: The key name to search for.
- `fileEncoding`: The encoding format of the file, default is 'utf-8'.

**Returns**:

The found value, or None if not found.

<a id="jtl_api.parseContent"></a>

## parseContent

```python
def parseContent(text):
```

Process the raw content by removing square brackets.

**Arguments**:

- `text`: The raw text.

**Returns**:

The processed text.