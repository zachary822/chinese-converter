# Chinese Converter

Converts between Traditional and Simplified Chinese. Uses monogram and bigram frequencies to pick optimal
words when a 1-to-1 conversion is not possible.

Uses phrases in the dictionary to count monogram and bigram frequencies.

## Installation

```bash
pip install chinese-converter
```

## Usage

```python
import chinese_converter

chinese_converter.to_traditional("simplified chinese text...")
chinese_converter.to_simplified("traditional chinese text...")

```

## Testing

```bash
python -m unittest
```

## License

MIT

## Resources

*Not necessary for the normal usage of this library.*

1. Dictionary Files: https://resources.publicense.moe.edu.tw/dict_reviseddict_download.html
