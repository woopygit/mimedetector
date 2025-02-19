# MIMEDetector

MIMEDetector is a Python library that makes it easy to detect MIME types of local files and remote URLs.

[Italian Documentation (Documentazione in Italiano)](README_IT.md)

## Installation

```bash
pip install mimedetector
```

## Usage

```python
from mimedetector import MIMEDetector

# English debug messages (default)
detector = MIMEDetector()

# Italian debug messages
detector_it = MIMEDetector(language="it")

# Check a local file
mime_type = detector.get_MIME("path/to/local/file.pdf")
print(f"Local file MIME type: {mime_type}")

# Check a remote URL
mime_type = detector.get_MIME("https://example.com/file.pdf")
print(f"URL MIME type: {mime_type}")
```

## Features

- Automatic detection between local files and remote URLs
- Support for Path and string paths
- Robust error handling
- Optional debugging for URL requests
- Multilanguage support (English and Italian)

## Requirements

- Python 3.7+
- requests

## License

This project is distributed under the MIT license.